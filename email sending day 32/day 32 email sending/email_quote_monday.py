some_text = """ My Social Network database should support all the basic functionalities of platforms such as Facebook, Instagram, Twitter. The plan is to create around 12 tables that will store all kinds of information about a user of the Social Network, information about the way they interact with the Social Network itself as well as other users of the Social Network.
Users should be able to create their profiles with information such as email, password, first name and last name and/or a username. Extra data should be stored for a user's profile such as their bio, location, interests, etc. There should also be several other tables about user's interation with the Network such as user's posts, notifications, event/activity log...There should be several tables about user's connections with other users that may be interconnected such as log of such connections, private messages, group chats and membership, comments, reactions...
While these are the basics of a Social Network database design, I may include special features for my Social Network database, for example: events that users would create that other users can pariticipate in.

"""

num_of_sentences = 0
for char in some_text:
    if char == ".":
        num_of_sentences += 1

print(num_of_sentences)
        