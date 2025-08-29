def twist():

    antall_personer = int(input("Hvor mange er dere på laget? "))
    twist_i_posen = int(input("Hvor mange twist er det i posen dere vant? "))

    twist_til_hver = twist_i_posen // antall_personer
    twist_til_overs = twist_i_posen % antall_personer

    print(
        f"Det blir {twist_til_hver} twist til hver, og det blir {twist_til_overs} twist til overs.")


twist()
