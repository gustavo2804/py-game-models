import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for key, info in players.items():
        player_name = key
        player_email = info.get("email")
        player_bio = info.get("bio")
        player_guild = info.get("guild")
        race = info.get("race")
        skills = race.get("skills")
        if race:
            Race.objects.get_or_create(
                name=race["name"],
                description=race["description"]
            )
        if skills:
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(
                        name=race["name"],
                        description=race["description"])
                )
        if player_guild:
            Guild.objects.get_or_create(
                name=player_guild["name"],
                description=player_guild["description"]
            )
        Player.objects.create(
            nickname=player_name,
            email=player_email,
            bio=player_bio,
            race=Race.objects.get(
                name=race["name"],
                description=race["description"]),
            guild=Guild.objects.get(
                name=player_guild["name"],
                description=player_guild["description"])
            if player_guild else None
        )


if __name__ == "__main__":
    main()
