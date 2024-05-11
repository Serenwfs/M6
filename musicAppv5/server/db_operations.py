import mysql.connector
import random
import datetime
import csv
from flask import Flask

class db_operations():
    
    def selectSongsByGenre(cur, genre):
        query = "SELECT * FROM Songs WHERE Genre_ID IN (SELECT Genre_ID FROM Genres WHERE Name = %s)"
        cur.execute(query, (genre,))
        return cur.fetchall()

    def selectSongsByMood(cur, mood):
        query = "SELECT * FROM Songs WHERE Mood_ID IN (SELECT Mood_ID FROM Moods WHERE Name = %s)"
        cur.execute(query, (mood,))
        return cur.fetchall()

    def createNewSong(cur, title, genre_id, mood_id, key_id):
        query = '''INSERT INTO Songs (Title, Genre_ID, Mood_ID, Key_ID) 
                    VALUES (%s, %s, %s, %s)'''
        cur.execute(query, (title, genre_id, mood_id, key_id))
        return cur.lastrowid


    # def getRandomSongElements(cur):
    #     query = '''SELECT * FROM Instrument_Tracks 
    #                 ORDER BY RAND() LIMIT 1'''
    #     cur.execute(query)
    #     return cur.fetchone()
    
    def selectSongsByCriteria(cur, genre, dancability): #TODO make sure the releasse staus is 1 
        dancability_min = dancability
        dancability_max = dancability + 0.30
        query = "SELECT * FROM SongDetails WHERE LOWER(genre) LIKE %s AND Dancability BETWEEN %s AND %s"
        criterias = [genre, dancability_min, dancability_max]
        cur.execute(query, criterias)
        return cur.fetchall()
    
    #TODO fect the genre, know from what song it's comming from checkn (in make song) release status, put random dancebility
    
    def selectRandomElements(cur, songs): 
        songIds = [song[0] for song in songs]
        song_id_string = ', '.join(str(id) for id in songIds)  #READ ME
        # for i in songIds:
        #     list += i
        # list = list[:-1]  # this reemove the last comma
        # print(list)

        query_instruments = f'''
        SELECT * FROM Instrument_Track 
        WHERE Song_ID IN ({song_id_string})
        ORDER BY RAND()
        LIMIT 2;
        '''
        cur.execute(query_instruments)
        instruments = cur.fetchall()

        lyrics = random.choice(songs)[3]
        genre_id = random.choice(songs)[5]
        print(instruments)

        return  lyrics, instruments, genre_id

#MOOD: Change those tow fucntion pour une containte mood the random

   
    def createNewSong(cur, title, lyrics, instruments, genre_id, user_id):

        key_id = 1  # TODO Placeholder Key_ID, assuming 1 is a valid key in your database
        creation_date = datetime.datetime.now().date()  # Get the current date
        released_status = False  # Default Released Status
        dancability = 0.0
        artist = "None"
        time_signature = 'None'
        # SQL query to insert a new song
        query = '''
        INSERT INTO Songs (Title, dancability, Artist, Genre_ID, Key_ID, User_ID, Lyrics, Creation_Date, Released_Status, Time_Signature)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        '''
        cur.execute(query, (title,dancability, artist, genre_id, key_id, user_id, lyrics, creation_date, released_status, time_signature))
        newSongid = cur.lastrowid  # the if of the new song


        print("Created New Song:")
        print(f"  Song ID: {newSongid}")
        print(f"  Title: {title}")
        print(f"  Genre ID: {genre_id}")
        print(f"  Key ID: {key_id}")  
        print(f"  Lyrics: {lyrics}")
        print(f"  Creation Date: {creation_date}")
        print(f"  Released Status: {released_status}")

        print("Associated Instruments:")
        # new we link the instruments to the new song
        for instrument in instruments:
            insert_instrument_query = '''
            INSERT INTO Instrument_Track (Name, Ethnic_Influence, Chord_Progression, Song_ID, Mood_ID)
            VALUES (%s, %s, %s, %s, %s);
            '''

        
            # Extract instrument data
            name = instrument[1]  # Adjust the index according to your actual data structure
            ethnic_influence = instrument[2]
            chord_progression = instrument[3]   
            mood_id = instrument[4]  # Adjust the index as needed
            cur.execute(insert_instrument_query, (name, ethnic_influence, chord_progression, newSongid, mood_id))
            print(f"  Name: {name}")
            print(f"  Ethnic Influence: {ethnic_influence}")
            print(f"  Chord Progression: {chord_progression}")
            print(f"  Song ID: {newSongid}")
            print(f"  Mood ID: {mood_id}\n")
                

        return newSongid
    
    
    def add_data_from_csv(cur, filepath, table_name):

            with open(filepath, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)  # Use DictReader to automatically handle columns
                columns = reader.fieldnames  # This should match the table columns
                if not columns:
                    print("No columns found in CSV file.")
                    return

                placeholders = ', '.join(['%s'] * len(columns))  # Create placeholders for SQL query
                columns_formatted = ', '.join(columns)  # Format columns for SQL syntax
                query = f"INSERT INTO {table_name} ({columns_formatted}) VALUES ({placeholders})"

                for row in reader:
                    # Extract values from the row, converting 'none' or empty strings to None
                    values = tuple((None if val.lower() == 'none' or val == '' else val) for val in (row[col] for col in columns))
                    try:
                        cur.execute(query, values)
                    except mysql.connector.Error as err:
                        print("Error inserting data: ", err)
                        print("Failed row: ", values)
                        continue  # Optionally continue or break depending on your need

                print(f"Data successfully added to {table_name}.")
       