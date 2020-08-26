#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct fighter{
	int hp;
	int dmg;
	int arm;
};

struct item{
	string name = "";
	int cost;
	int dmg;
	int arm; 
};

void getItemSets(vector<item>& itemSets, const vector<item>& weapons,
	const vector<item>& armor, const vector<item>& rings);

bool compareByCost(const item& a, const item& b);

bool winFight(fighter player, fighter boss);

int main(){

	fighter boss;
	boss.hp = 109;
	boss.dmg = 8;
	boss.arm = 2;

	fighter player;
	player.hp = 100;

	vector<item> weapons;
	weapons.push_back({"Dagger", 8, 4, 0});
	weapons.push_back({"Shortsword", 10, 5, 0});
	weapons.push_back({"Warhammer", 25, 6, 0});
	weapons.push_back({"Longsword", 40, 7, 0});
	weapons.push_back({"Greataxe", 74, 8, 0});

	vector<item> armor;
	armor.push_back({"Leather", 13, 0, 1});
	armor.push_back({"Chainmail", 31, 0, 2});
	armor.push_back({"Splintmail", 53, 0, 3});
	armor.push_back({"Bandedmail", 75, 0, 4});
	armor.push_back({"Platemail", 102, 0, 5});

	vector<item> rings;
	rings.push_back({"Damage +1", 25, 1, 0});
	rings.push_back({"Damage +2", 50, 2, 0});
	rings.push_back({"Damage +3", 100, 3, 0});
	rings.push_back({"Defense +1", 20, 0, 1});
	rings.push_back({"Defense +2", 40, 0, 2});
	rings.push_back({"Defense +3", 80, 0, 3});

	vector<item> itemSets;
	getItemSets(itemSets, weapons, armor, rings);
	sort(itemSets.begin(), itemSets.end(), compareByCost);

	// Part 1
	for (auto item : itemSets){

		player.dmg = item.dmg;
		player.arm = item.arm;

		if (winFight(player, boss)){
			cout << "Least amount of gold needed to win: " << item.cost << endl;
			break;
		}
	}

	// Part 2
	sort(itemSets.rbegin(), itemSets.rend(), compareByCost);

	for (auto item : itemSets){

		player.dmg = item.dmg;
		player.arm = item.arm;

		if (!winFight(player, boss)){
			cout << "Most amount of gold that can be spent on a loss: " << item.cost << endl;
			break;
		}
	}

}

void getItemSets(vector<item>& itemSets, const vector<item>& weapons,
	const vector<item>& armor, const vector<item>& rings){

	// 1 weapon
	for (auto weapon : weapons){

		item w;
		w.cost = weapon.cost;
		w.dmg = weapon.dmg;
		w.arm = weapon.arm;

		// 0 - 1 armor
		for (int i = -1; i < (int) armor.size(); i++){

			item wa = w;
			if (i > -1){
				wa.cost += armor[i].cost;
				wa.arm += armor[i].arm;
			}

			// 0 - 2 rings
			for (int j = -1; j < (int) rings.size(); j++){

				item war = wa;
				if (j > -1){
					war.cost += rings[j].cost;
					war.dmg += rings[j].dmg;
					war.arm += rings[j].arm;
				}

				for (int k = -1; k < (int) rings.size(); k++){

					item warr = war;
					if (k > -1 && k == j){
						continue;
					}
					if (k > -1){
						warr.cost += rings[k].cost;
						warr.dmg += rings[k].dmg;
						warr.arm += rings[k].arm;
					}

					itemSets.push_back(warr);
				}
			}
		}
	}
}

bool compareByCost(const item& a, const item& b){
	return a.cost < b.cost;
}

bool winFight(fighter player, fighter boss){
	while (true) {

		boss.hp -= player.dmg - boss.arm > 1 ? player.dmg - boss.arm : 1;
		if (boss.hp <= 0){
			return true;
		}

		player.hp -= boss.dmg - player.arm > 1 ? boss.dmg - player.arm : 1;
		if (player.hp <= 0){
			return false;
		}
	}
}