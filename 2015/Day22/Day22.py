import copy 

class Wizard:

    def __init__(self, hp, mana):
        self.hp = hp
        self.mana = mana
        self.armor = 0
        self.shield_cooldown = 0
        self.poison_cooldown = 0
        self.recharge_cooldown = 0

    def move(self, spell, boss):

        # Hard mode
        self.hp -= 1

        # Effects
        if self.shield_cooldown > 0:
            self.shield_cooldown -= 1
            if self.shield_cooldown > 0:
                self.armor = 7
            else:
                self.armor = 0

        if self.poison_cooldown > 0:
            self.poison_cooldown -= 1
            boss.hp -= 3

        if self.recharge_cooldown > 0:
            self.recharge_cooldown -= 1
            self.mana += 101

        # Spell
        self.mana -= spell["cost"]

        if spell["name"] == 'missile':
            boss.hp -= 4

        elif spell["name"]  == 'drain':
            boss.hp -= 2
            # Don't heal if already dead
            if self.hp > 0:
                self.hp += 2

        elif spell["name"]  == 'shield':
            self.shield_cooldown = 6

        elif spell["name"]  == 'poison':
            self.poison_cooldown = 6

        elif spell["name"]  == 'recharge':
            self.recharge_cooldown = 5

class Boss:
    def __init__(self, hp, dmg):
        self.hp = hp
        self.dmg = dmg

    def move(self, wizard):

        # Effects
        if wizard.shield_cooldown > 0:
            wizard.shield_cooldown -= 1
            if wizard.shield_cooldown > 0:
                wizard.armor = 7
            else:
                wizard.armor = 0

        if wizard.poison_cooldown > 0:
            wizard.poison_cooldown -= 1
            self.hp -= 3

        if wizard.recharge_cooldown > 0:
            wizard.recharge_cooldown -= 1
            wizard.mana += 101

        # Attack
        wizard.hp -= max(self.dmg - wizard.armor, 1)

class TreeNode:
    def __init__(self, spell, total_cost, game_status, wizard, boss):
        self.spell = spell
        self.total_cost = total_cost
        self.game_status = game_status
        self.wizard = wizard
        self.boss = boss
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def get_leaves(self, game_status):
        leaves = []
        def _get_leaves(node):
            if node is not None:
                if len(node.children) == 0 and node.game_status == game_status:
                    leaves.append(node)
                for n in node.children:
                    _get_leaves(n)
        _get_leaves(self)
        return leaves

def main():

    wizard = Wizard(50, 500)
    boss = Boss(51, 9)

    spells = [{"name" : "missile", "cost" : 53},
              {"name" : "drain", "cost" : 73},
              {"name" : "shield", "cost" : 113},
              {"name" : "poison", "cost" : 173},
              {"name" : "recharge", "cost" : 229},]

    root = TreeNode(None, 0, "ongoing", wizard, boss)
    leaves = [root] 

    min_cost = 99999

    while(leaves):

        for leaf in leaves:

            for spell in spells:

                new_wizard = copy.copy(leaf.wizard)
                new_boss = copy.copy(leaf.boss)
                new_cost = leaf.total_cost + spell["cost"]

                # Can't cast a spell that's in cooldown
                if spell["name"] == "shield" and new_wizard.shield_cooldown > 1:
                    continue
                if spell["name"] == "poison" and new_wizard.poison_cooldown > 1:
                    continue
                if spell["name"] == "recharge" and new_wizard.recharge_cooldown > 1:
                    continue

                game_status = "ongoing"

                # Ignore paths that are already more expensive than cheapest win
                if new_cost > min_cost:
                    game_status = "expensive"

                new_wizard.move(spell, new_boss)

                # Check death due to hard mode
                if new_wizard.hp <= 0:
                    game_status = "lost"

                new_boss.move(new_wizard)
                
                if game_status == "ongoing":
                    if new_wizard.mana < 0:
                        game_status = "lost"
                    elif new_boss.hp <= 0:
                        game_status = "won"
                        min_cost = min(new_cost, min_cost)
                    elif new_wizard.hp <= 0:
                        game_status = "lost"

                node = TreeNode(spell, new_cost, game_status, new_wizard, new_boss)
                leaf.add_child(node)

        leaves = root.get_leaves("ongoing")

    print(min_cost)

main()