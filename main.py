# requirements
# - display weekly money
# - add money on a monday
# - allow money to be taken away

import parts.tools as Tools
import parts.visuals as Visuals

if __name__ == "__main__":

    standing_order, extra = 50.0, 61.5
    safe, warning, critical = 80, 61.5, 30

    print("")

    # welcome message
    Tools.SetWeeklyMoney(standing_order, extra)
    if Tools.GetDay() == "Monday" and Tools.GetRuntimeStatus():
        print(Visuals.DisplayMessage("info", False, "It's a new week! Money has been set to your weekly maximum."))
    else:
        print(Visuals.DisplayMessage("info", False, "Welcome back!"))

    # message for money remaining
    print(f"\nYou currently have £{Tools.Fround(Tools.GetMoney())}")
    if Tools.GetMoney() > safe:
        print("This puts you in the safe zone. Nice work!")
    elif Tools.GetMoney() > warning:
        print("This puts you in the warning zone. You're approaching your advised weekly budget, so be careful.")
    elif Tools.GetMoney() > critical:
        print("This puts you in the critical zone. Make future purchases only if completely necessary.")
    else:
        print("You've surpassed your critical limit. Please re-evaluate what you are spending your money on for next week.")

    query = input(Visuals.DisplayMessage("query", True, "What would you like to do? [h for help]")).strip().lower()
    match query:

        case "h":
            print(f"""
    {Visuals.DisplayMessage("positive", False, "Help menu")}
    Welcome to the help menu. Below are all the commands that are currently available in this version.

    remove 
        Moves you to the money removal menu.
        This is where you enter how much you've spent.

    {Visuals.DisplayMessage("info", False, "To get back to the main finance menu, please rerun this program.")}
            """)

        case "remove":
            print(f"""
    {Visuals.DisplayMessage("positive", False, "Removal menu")}
    Welcome to the removal menu. Every day, make sure you've kept track of how much you have spent.
            """)

            deduct = float(input(Visuals.DisplayMessage("", True, "Please enter the amount you have spent")))
            Tools.RemoveMoney(deduct)

            print(f"\nThanks for the update! You now have £{Tools.Fround(Tools.GetMoney())} remaining.")
            next_zone = ""
            if Tools.GetMoney() > safe: zone = "safe"
            elif Tools.GetMoney() > warning: zone = "warning"
            elif Tools.GetMoney() > critical: zone = "critical"
            else: zone = "urgent"
            print(Visuals.DisplayMessage("alert", False, f"Heads up ! \tYour next zone is the {zone} zone.\n"))

    pass
