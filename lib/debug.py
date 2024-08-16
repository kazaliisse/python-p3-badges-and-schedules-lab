from conference_badges import (
    badge_maker, batch_badge_creator,
    assign_rooms, printer
)

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()
    names = ["Arel", "Carol", "Jim", "Pam"]
    
    # Test badge_maker function
    print(badge_maker("Arel"))

    # Test batch_badge_creator function
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)
    
    # Test assign_rooms function
    rooms = assign_rooms(names)
    for room in rooms:
        print(room)
    
    # Test printer function
    printer(names)
