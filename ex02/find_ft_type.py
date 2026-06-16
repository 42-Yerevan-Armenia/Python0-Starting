def all_thing_is_obj(object: any) -> int:
    if isinstance(object, str):
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        if isinstance(object, int):
            print("Type not found")
        else:
            print(f"{object.__class__.__name__.capitalize()} : {type(object)}")
    return 42
