from project.team import Team
from unittest import TestCase, main


class Test(TestCase):
    def test_init_name(self):
        team = Team("Test")
        self.assertEqual("Test", team.name)
        team.members = {}
        self.assertEqual({}, team.members)

    def test_init_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            team = Team("123")
        expected_res = "Team Name can contain only letters!"
        self.assertEqual(expected_res, str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            team = Team("1Kld1")
        expected_res = "Team Name can contain only letters!"
        self.assertEqual(expected_res, str(ex.exception))

    def test_adding_members_properly(self):
        team = Team("Test")
        team.members = {}
        test_dict = {"A": 3, "B": 4}
        team.add_member(**test_dict)
        self.assertEqual({"A": 3, "B": 4}, team.members)

    def test_not_adding_members_if_it_already_exists(self):
        team = Team("Test")
        team.members = {"A": 3}
        test_dict = {"A": 3, "B": 4}
        team.add_member(**test_dict)
        self.assertEqual({"A": 3, "B": 4}, team.members)

    def test_adding_members_str_return(self):
        team = Team("Test")
        team.members = {"C": 4}
        test_dict = {"A": 3, "B": 4}

        result = team.add_member(**test_dict)
        expected_res = f"Successfully added: A, B"

        self.assertEqual(expected_res, result)

    def test_remove_member_if_they_are_in_the_list(self):
        team = Team("Test")
        team.members = {"C": 4, "B": 2}
        name = "B"
        expected_res = f"Member {name} removed"
        result = team.remove_member(name)
        self.assertEqual(expected_res, result)

    def test_remove_members_does_properly_del_member(self):
        team = Team("Test")
        team.members = {"C": 4, "B": 2}
        name = "B"
        expected_res = {"C": 4}
        team.remove_member(name)
        self.assertEqual(expected_res, team.members)

    def test_remove_members_if_the_name_does_not_exist(self):
        team = Team("Test")
        team.members = {"C": 4, "B": 2}
        name = "A"
        expected_res = f"Member with name {name} does not exist"
        result = team.remove_member(name)
        self.assertEqual(expected_res, result)

    def test__gt__False(self):
        team = Team("Test")
        team_2 = Team("TestSecondTeam")
        team.members = {"C": 4, "B": 2}
        team_2.members = {"G": 4, "A": 2, "D": 2}

        res = len(team.members) > len(team_2.members)
        self.assertFalse(False, res)

    def test__gt__True(self):
        team = Team("Test")
        team_2 = Team("TestSecondTeam")
        team.members = {"C": 4, "B": 2}
        team_2.members = {"G": 4}

        res = len(team.members) > len(team_2.members)
        self.assertTrue(True, res)

    def test_does__len__returns_len_properly(self):
        team = Team("Test")
        team.members = {"C": 4, "B": 2}
        exp_res = 2
        res = team.__len__()
        self.assertEqual(exp_res, res)

    def test_string_representation(self):
        team = Team("Test")
        team.members = {"C": 4, "B": 2}
        result = [f"Team name: {team.name}"]
        members = list(sorted(team.members.items(), key=lambda x: (-x[1], x[0])))
        result.extend([f"Member: {x[0]} - {x[1]}-years old" for x in members])
        expected_res = "\n".join(result)
        self.assertEqual(expected_res, str(team))


if __name__ == "__main__":
    main()