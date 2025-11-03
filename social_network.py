class Person:
    # Represents one user in the network
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        # Adds a friend if not already added
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    # Represents the overall social network using a graph (adjacency list)
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        # Adds a new person if they don't already exist
        if name not in self.people:
            self.people[name] = Person(name)
        else:
            print(f"{name} already exists in the network.")

    def add_friendship(self, person1_name, person2_name):
        # Creates a two-way friendship if both people exist
        if person1_name not in self.people or person2_name not in self.people:
            print(f"Friendship not created. One or both users not found ({person1_name}, {person2_name}).")
            return

        p1 = self.people[person1_name]
        p2 = self.people[person2_name]
        p1.add_friend(p2)
        p2.add_friend(p1)

    def print_network(self):
        # Displays all users and their friends
        for name, person in self.people.items():
            friends_names = [f.name for f in person.friends]
            if friends_names:
                print(f"{name} is friends with: {', '.join(friends_names)}")
            else:
                print(f"{name} has no friends yet.")


# Example usage / tests
if __name__ == "__main__":
    network = SocialNetwork()

    # Add people
    network.add_person("Alex")
    network.add_person("Jordan")
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")
    network.add_person("Alex")  # Duplicate person test

    # Create friendships
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Jordan", "Johnny")  # One user doesn’t exist
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    print("\n--- Social Network ---")
    network.print_network()


# Design Memo 
'''
A graph is the ideal structure for representing a social network because it models relationships as 
connections between people (nodes). Friendships in real life are mutual, and graphs naturally represent 
these bidirectional relationships using edges between nodes. This allows for flexible connections and 
makes it easy to visualize or analyze how people are linked — such as finding mutual friends or suggesting 
new ones based on shared connections.

Lists or trees would not work as effectively. A list could store people, but it can’t easily represent 
complex, interconnected relationships. To find friends or mutual connections, you would need to manually 
search through multiple lists, which becomes inefficient as the network grows. A tree structure enforces 
a hierarchy with a single parent-child relationship, which doesn’t reflect how friendships work — people 
can have many connections across different branches without a central root.

When adding friends or printing the network, performance trade-offs appear mostly in the time it takes to 
traverse and display connections. Adding a person or creating a friendship is efficient (constant time for 
dictionary lookups), but printing large networks can become slower because each person’s friends list must 
be processed. Overall, the adjacency list representation offers a great balance between speed, clarity, 
and scalability for modeling dynamic, real-world social relationships.
'''
