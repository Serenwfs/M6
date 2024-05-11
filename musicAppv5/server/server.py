# import MySQL
import mysql.connector
from flask import Flask, request, jsonify, Blueprint
import random
from db_operations import db_operations
from helper import helper
from flask import Flask, request, jsonify, session
from flask_session import Session  # Ensure Flask-Session is installed and imported
from flask_cors import CORS, cross_origin
import logging
import bcrypt
import json
import os
import secrets
from flask import Flask, request, jsonify
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, \
                               unset_jwt_cookies, jwt_required, JWTManager


# # Generate a secret key
secret_key = secrets.token_urlsafe(16)  # Generates a secure random URL-safe base64-encoded key

# print("Secret Key:", secret_key)



def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(provided_password, stored_password):
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))



app = Flask(__name__)

# app.secret_key = secrets.token_urlsafe(16)
app.config["JWT_SECRET_KEY"] = secret_key

# logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w',
#                     format='%(name)s - %(levelname)s - %(message)s')



# JWT configuration

CORS(app, supports_credentials=True)

jwt = JWTManager(app)
# Configure session to use filesystem (Flask-Session)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
server_session = Session(app)

@app.route("/api/home", methods=['GET'])
def return_home():
    return jsonify({
        'message': "Hello world!"
    } )


@app.route('/protected')
@jwt_required()  # This decorator ensures that the JWT is checked before the function runs
def protected():
    user_identity = get_jwt_identity()  # Now you can safely call get_jwt_identity()
    return jsonify(logged_in_as=user_identity), 200

@app.route('/')
def index():
    return "Welcome to the Song Maker App!"

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="CPSC408!",
        database="MusicApp",
        auth_plugin='mysql_native_password'
    )


@app.route('/songs', methods=['GET'])
def get_songs():
    genre = request.args.get('genre', default=None, type=str)
    cur = conn.cursor()
    songs = db_operations.selectSongsByGenre(cur, genre) if genre else []
    cur.close()
    conn.close()
    return jsonify(songs)

@app.route('/create_song', methods=['POST'])
def createNewSong():
    data = request.json
    cur = conn.cursor()
    new_song_id = db_operations.createNewSong(cur, data['title'], data['instruments'], data['lyrics'], data['genre_id'])
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Song created successfully", "song_id": new_song_id})


###
# '''CODE TO FIRST CONNECT AND CREATE DATABASE'''
# #Make first Connection
# conn = mysql.connector.connect(host="localhost",
# user="root",
# password="CPSC408!",
# auth_plugin='mysql_native_password')
# #create cursor object
# cur_obj = conn.cursor()
# #create database schema
# cur_obj.execute("CREATE SCHEMA MusicApp;")
# #confirm execution worked by printing result
# cur_obj.execute("SHOW DATABASES;")
# for row in cur_obj:
#     print(row)
# #Print out connection to verify and close
# print(conn)
# conn.close()
# ''' END '''


#Make Connection
conn = mysql.connector.connect(host="localhost",
user="root",
password="CPSC408!",
auth_plugin='mysql_native_password',
database="MusicApp")
#create cursor object
cur_obj = conn.cursor()
#Print out connection to verify and close
print(conn)



def createTables(cur_obj):


    # '''CREATING AND POPULATING TABLES WITH SAMPLE DATA'''

    # query1 = ''' 
    #     CREATE TABLE Song_Maker(
    #         User_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    #         Username VARCHAR(50),
    #         Email VARCHAR(50),
    #         Password CHAR(64) NOT NULL
    #         );
    #     '''
    # cur_obj.execute(query1)

    # query2 = ''' 
    #     CREATE TABLE Mood(
    #         Mood_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    #         Name VARCHAR(50)
    #         );
    #     '''
    # cur_obj.execute(query2)


    # query3 = ''' 
    #     CREATE TABLE Genres(
    #         Genre_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    #         Name VARCHAR(50)
    #         );
    #     '''
    # cur_obj.execute(query3)



    # query4 = ''' 
    #     CREATE TABLE Musical_Keys(
    #         Key_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    #         Name VARCHAR(50),
    #         Note1 VARCHAR(10),
    #         Note2 VARCHAR(10),
    #         Note3 VARCHAR(10),
    #         Note4 VARCHAR(10),
    #         Note5 VARCHAR(10),
    #         Note6 VARCHAR(10),
    #         Note7 VARCHAR(10),
    #         Mood_ID INT, 
    #         FOREIGN KEY (Mood_ID) REFERENCES Mood(Mood_ID)
    #         );
    #     '''
    # cur_obj.execute(query4)


    # query5 = ''' 
    #     CREATE TABLE Songs(
    #         Song_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    #         Title VARCHAR(50),
    #         Dancability FLOAT,
    #         Artist VARCHAR(50), 
    #         Genre_ID INT,
    #         Key_ID INT,
    #         User_ID INT,
    #         Lyrics TEXT,
    #         Creation_Date DATE, 
    #         Released_Status BOOL,
    #         Time_Signature VARCHAR(10),
    #         FOREIGN KEY (Genre_ID) REFERENCES Genres(Genre_ID),
    #         FOREIGN KEY (Key_ID) REFERENCES Musical_Keys(Key_ID),
    #         FOREIGN KEY (User_ID) REFERENCES Song_Maker(User_ID)
    #         );
    #     '''
    # cur_obj.execute(query5)
    

    # query6 = ''' 
    #     CREATE TABLE Instrument_track(
    #         Instrument_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    #         Name VARCHAR(50),
    #         Ethnic_Influence VARCHAR(50),
    #         Chord_Progression VARCHAR(50),
    #         Song_ID INT,
    #         Mood_ID INT,
    #         FOREIGN KEY (Song_ID) REFERENCES Songs(Song_ID),
    #         FOREIGN KEY (Mood_ID) REFERENCES Mood(Mood_ID)
    #         );
    #     '''
    # cur_obj.execute(query6)

    # #  Insert data into user
    # user = [
    #     ('Lala', 'lala@gmail.com', 'coco123'),
    #     ('WillSmith', 'will.smith@gmail.com', 'lilalila'),
    #     ('Alicekeys', 'alicekeys@gmail.com', 'bibi' )
    #         ]
    # cur_obj.executemany("INSERT INTO Song_Maker(Username, Email, Password) VALUES (%s, %s, %s);", user)
    # conn.commit()

    # db_operations.add_data_from_csv(cur_obj, "MoodTable.csv", "Mood")
    # conn.commit()
   
    # db_operations.add_data_from_csv(cur_obj, "GenresTable.csv", "Genres")
    # conn.commit()
    
    # db_operations.add_data_from_csv(cur_obj, "Musical_KeysTable.csv", "Musical_Keys")
    # conn.commit()

    # db_operations.add_data_from_csv(cur_obj, "SongTable.csv", "Songs")
    # conn.commit()
    db_operations.add_data_from_csv(cur_obj, "InstrumentTable.csv", "Instrument_track")
    conn.commit()
   


#     '''END OF THE COMMENTS: to create the tables and sample data '''


def createView(cur_obj):
    query = '''
    CREATE VIEW SongDetails AS
    SELECT 
        s.Song_ID, s.Title, s.Dancability, s.Lyrics, s.Creation_Date, s.Released_Status, s.Time_Signature,
        g.Name AS Genre,
        k.Name AS KeyName
    FROM Songs s
    JOIN Genres g ON s.Genre_ID = g.Genre_ID
    JOIN Musical_Keys k ON s.Key_ID = k.Key_ID;
    '''

    cur_obj.execute(query)
    print("View 'SongDetails' created successfully.")


@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        if datetime.fromtimestamp(exp_timestamp, timezone.utc) < now + timedelta(minutes=30):
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_token"] = access_token
                response.data = json.dumps(data)
    except (RuntimeError, KeyError):
        # No valid JWT available, just return the original response
        pass
    return response



@app.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    
    hashed_password = hash_password(password)

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO Song_Maker (Username, Email, Password) VALUES (%s, %s, %s)",
                    (username, email, hashed_password))
        conn.commit()
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 400
    finally:
        cur.close()
        conn.close()
    
    return jsonify({"message": "User registered successfully"}), 201



@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT Password, User_ID FROM Song_Maker WHERE Username = %s", (username,))
            user = cur.fetchone()
            
            if user and check_password(password, user[0]):
                access_token = create_access_token(identity={'user_id': user[1], 'username': username})
                return jsonify(access_token=access_token), 200
            else:
                return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn.is_connected():
            conn.close()


@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove user_id from session
    return 'Logged Out'

@app.route('/api/make_song', methods=['POST'])
@jwt_required()
def make_song():
   
    data = request.json
    app.logger.debug(f"Received data: {data}")
    print(f"ReceiveD data: {data}")
    # logging.debug("Receiveed data: %s", data)
    # app.logger.debug("Receivd data: %s", data)
    genre = data.get('genre', '').lower()
    dancability_input = int(data.get('dancability', 1))
    dancability = [0.25, 0.50, 0.75][dancability_input - 1]
    print(f"ReceiveD data: ", dancability)
    
    # Get user identity from JWT
    user_identity = get_jwt_identity()
    user_id = user_identity['user_id']  # Adjust according to how you set up JWT identity
    print("1 ")
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                print("2")
                formattedInput = f"%{genre}%".lower()
                songs = db_operations.selectSongsByCriteria(cur, formattedInput, dancability)
                if not songs:
                    return jsonify({"error": "No songs found with the specified criteria."}), 404
    
                print("3 ")
                result = db_operations.selectRandomElements(cur, songs)
                if result is None or len(result) < 3:
                    print("selectRandomElements returned insufficient data.")
                    return jsonify({"error": "Internal error processing song elements."}), 500
                print("4")
                lyrics, instruments, genre_id = result 
                print("Executing SQL with instruments: %s", instruments)
                if not instruments:
                    return jsonify({"error": "No instruments provided"}), 400
                
                print("inst: ",instruments)

                instrument_details = [{
                    'name': i[1],
                    'ethnic_influence': i[2],
                    'chord_progression': i[3] #SOUND
                } for i in instruments]

                print("inst: ",instrument_details)

                title = data.get('title', 'Untitled Song')
                new_song_id = db_operations.createNewSong(cur, title, lyrics, instruments, genre_id, user_id) 
                conn.commit()

                cur.execute("SELECT Song_ID, Title, Dancability, Artist, Genre_ID, Key_ID, User_ID, Lyrics, Creation_Date, Released_Status, Time_Signature FROM Songs WHERE Song_ID = %s", (new_song_id,))
                song = cur.fetchone()

        # Ensuring data is fetched within the cursor context
        return jsonify({
            "message": "Created new song successfully",
            "song_details": {
                "Title": song[1],
                "Dancability": song[2],
                "Artist": song[3],
                "Lyrics": song[7],
                "Creation_Date": song[8],
                "Released_Status": "Released" if song[9] else "Not Released",
                "Time_Signature": song[10],
                "instruments": instrument_details
            }
        }), 201
    except Exception as e:
        logging.error("Error processing the make_song request: %s", e)
        return jsonify({"error": "An error occurred processing your request"}), 500


@app.route('/api/genres', methods=['GET'])
def get_genres():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT Genre_ID, Name FROM Genres")
        genres = cur.fetchall()
        return jsonify([{"id": genre[0], "name": genre[1]} for genre in genres]), 200
    except Exception as e:
        logging.error("Failed to fetch genres: %s", e)
        return jsonify({"error": "Failed to fetch genres"}), 500
    finally:
        cur.close()
        conn.close()


def pretty_print_songs(songs):
    if not songs:
        print("No songs found for this genre.")
    else:
        for song in songs:
            print("\nSong Details:")
            print(f"  ID: {song[0]}")
            print(f"  Title: {song[1]}")
            print(f"  Dancability: {song[2]}")
            print(f"  Artist: {song[3]}")
            print(f"  Genre_ID: {song[4]}")
            print(f"  Key_ID: {song[5]}")
            print(f"  User_ID: {song[6]}")
            print(f"  Lyrics: {song[7][:50]}...")  #  only the first 50 characters of the lyrics
            print(f"  Creation_Date: {song[8]}")
            print(f"  Released_Status: {'Released' if song[9] else 'Not Released'}")
            print(f"  Time_Signature: {song[10]}")


def main_menu(cur_obj):
    print("Welcome to the Song Maker App")
    print("1. Search Songs by Genre")
    print("2. Create a New Song")
    print("3. Exit")
    choice = helper.get_choice([1,2,3])

    if choice == 1:
        genre = input("Enter the genre: ")
        songs = db_operations.selectSongsByGenre(cur_obj, genre)
    
        pretty_print_songs(songs)

    elif choice == 2:
        # makeSong(cur_obj) 
        make_song()
    
# createTables(cur_obj)
# createView(cur_obj)
# main_menu(cur_obj)



def drop_database():
    # Make Connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="CPSC408!",
        auth_plugin='mysql_native_password'
    )
    # Create cursor object
    cur_obj = conn.cursor()
    
    # Drop the database
    try:
        cur_obj.execute("DROP DATABASE MusicApp;")
        print("Database 'MusicApp' dropped successfully.")
    except mysql.connector.Error as err:
        print("Failed to drop database: {}".format(err))
    finally:
        # Close the cursor and connection
        cur_obj.close()
        conn.close()

# drop_database()


cur_obj.close()
conn.close()

if __name__ == '__main__':
    app.run(debug=True)