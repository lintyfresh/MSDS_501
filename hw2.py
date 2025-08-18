spotify = {
    1: {"artists": ["ROSÉ", "Bruno Mars"], "title": "APT.", "length": "2:49"},
    2: {"artists": ["Lady Gaga", "Bruno Mars"], "title": "Die With a Smile",
        "length": "4:11"},
    3: {"artists": ["Ed Sheeran"], "title": "Sapphire", "length": "2:59"},
    4: {"artists": ["Billie Eilish"], "title": "Birds of a Feather",
        "length": "3:30"},
    5: {"artists": ["Benson Boone"], "title": "Beautiful Things",
        "length": "3:00"},
    6: {"artists": ["Sabrina Carpenter"], "title": "Manchild",
        "length": "3:33"},
    7: {"artists": ["Alex Warren"], "title": "Ordinary", "length": "3:06"},
    8: {"artists": ["Billie Eilish"], "title": "Wildflower", "length": "4:21"},
    9: {"artists": ["Sabrina Carpenter"], "title": "Espresso",
        "length": "2:55"},
    10: {"artists": ["Lady Gaga"], "title": "Abracadabra", "length": "3:43"}
}

while True:
    choice = input("Enter what you would like to browse:\n \
                            \t1: A list of artists in the top 10 most played songs\n \
                            \t2: Song by ranking\n \
                            \t3: Songs by an artist\n \
                            \t4: Songs ordered by length\n \
                            \t0: Exit\n")

    choice = int(choice)

    top_artists =[]

    if choice == 1:
        for key, value in spotify.items():
            for artist in spotify[key]["artists"]:
                if artist not in top_artists:
                    top_artists.append(artist)

        top_artists.sort()
        final_output = ""

        for artists in top_artists:
            final_output += artists
            final_output += ", "
                
        print(final_output.strip(' ,'))

    if choice == 2:
        ranking_question = input("Enter the ranking you're interested in (between 1 and 10): ")
        try:
            ranking = int(ranking_question)
            #print(ranking)
            nums = [1,2,3,4,5,6,7,8,9,10]
            if ranking in nums:
                for key, value in spotify.items():
                    if key == ranking:
                        title = spotify[key]["title"]
                        artists_string = ", ".join(spotify[key]["artists"])
                        print(f"{ranking}: {title} by {artists_string}")

            else:
                ranking_range_error = "Ranking out of range."
                print(ranking_range_error)
            
        except ValueError:
            ranking_value_error = "Invalid input. Please enter a number."
            print(ranking_value_error)
    
    if choice == 3:
        artist_question = input("Enter the name of the artist you're interested in: ")

        artist_input2 = artist_question

        artist_input = artist_question.lower()

        artist_list = []

        for key, value in spotify.items():
            for artist in spotify[key]["artists"]:
                if artist not in artist_list:
                    artist_list.append(artist.lower())
    
        if artist_input in artist_list:
            for key, value in spotify.items():
                for artists in spotify[key]["artists"]:
                    if artists.lower() == artist_input:
                        song_title = spotify[key]["title"]
                        print(f"{key}: {song_title}")
        else:
            artist_error = "No songs were found by "
            print(artist_error + artist_input2)
    
    if choice == 4:
        length_question = input("Enter a number to view songs by length. (Positive: longest songs, Negative: shortest songs): ")
        try:
            user_input = int(length_question)

            list_of_times = list()
    
            for key, value in spotify.items():
                minute = int(spotify[key]["length"].split(":")[0])
                second = int(spotify[key]["length"].split(":")[1])
                total_time = minute * 60 + second
                list_of_times.append(total_time)

            #print(list_of_times)

            if(user_input >= 0):
                list_of_times.sort(reverse=True)
                #print(list_of_times)
            else:
                list_of_times.sort()
                #print(list_of_times)
            
            #print(list_of_times)
            
            ind = abs(user_input)

            new_list = list_of_times[0:ind]
            
            for times in new_list:
                for key, value in spotify.items():
                    minute = int(spotify[key]["length"].split(":")[0])
                    second = int(spotify[key]["length"].split(":")[1])
                    total_time = minute * 60 + second
                    if times == total_time:
                        title = spotify[key]["title"]
                        artists_string = ", ".join(spotify[key]["artists"])
                        print(f"{title} by {artists_string} ({total_time} seconds)")
            break

        except ValueError:
            length_value_error = "Invalid value. Please enter a number."
            print(length_value_error)

    if choice == 0:
        break

