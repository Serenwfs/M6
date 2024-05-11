import React, { useState, useEffect } from 'react';
import styles from './CreateSong.module.css';

export default function CreateSong() {
    const [genres, setGenres] = useState([]);
    const [selectedGenre, setSelectedGenre] = useState('');
    const [dancability, setDancability] = useState('1');  // Default to 'Not really danceable'
    const [title, setTitle] = useState('');
    const [message, setMessage] = useState('');
    const [songDetails, setSongDetails] = useState(null);

    useEffect(() => {
        const token = localStorage.getItem('token'); // Ensure the token is actually being retrieved
        console.log("Token sent with request:", token); // Debugging line
        if (!token) {
            console.log('No token found, user might not be logged in');
            return;
        }
        fetch('http://127.0.0.1:5000/api/genres', {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch genres');
            }
            return response.json();
        })
        .then(data => setGenres(data))
        .catch(error => {
            console.error('Error fetching genres:', error);
            setMessage('Failed to load genres');
        });
    }, []);

    const handleSubmit = async (event) => {
        event.preventDefault();
        const token = localStorage.getItem('token');
        
        if (!token) {
            setMessage('No authentication token found. Please log in again.');
            return;
        }
        try {
            const response = await fetch('http://127.0.0.1:5000/api/make_song', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({
                    genre: selectedGenre,  
                    dancability: dancability,
                    title: title
                })
            });
            console.log("Sending payload:", JSON.stringify({
                genre: selectedGenre,  
                dancability: dancability,
                title: title
            }));
    
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status} - ${response.statusText}`);
            }
    
            const data = await response.json();
            setMessage("Song created successfully!");
            setSongDetails(data.song_details);
        } catch (error) {
            console.error('Fetch error:', error);
            setMessage(error.message || 'Failed to fetch');
            setSongDetails(null);
        }
    };

//      return (
//         <div className={styles.container}>
//             <h1 className={styles.title}>Create a New Song</h1>
//             <form onSubmit={handleSubmit} className={styles.form}>
//                 <div className={styles.inputField}>
//                     <label>Genre:</label>
//                     <select className={styles.select} value={selectedGenre} onChange={(e) => setSelectedGenre(e.target.value)}>
//                         <option value="">Select a Genre</option>
//                         {genres.map(genre => (
//                             <option key={genre.id} value={genre.name}>{genre.name}</option>
//                         ))}
//                     </select>
//                 </div>
//                 <div className={styles.inputField}>
//                     <label>Dancability:</label>
//                     <select className={styles.select} value={dancability} onChange={(e) => setDancability(e.target.value)}>
//                         <option value="1">Not really danceable</option>
//                         <option value="2">Somewhat Danceable</option>
//                         <option value="3">Very Danceable</option>
//                     </select>
//                 </div>
//                 <div className={styles.inputField}>
//                     <label>Title:</label>
//                     <input type="text" className={styles.input} value={title} onChange={(e) => setTitle(e.target.value)} />
//                 </div>
//                 <button type="submit" className={styles.button}>Create Song</button>
//                 {message && <p className={styles.message}>{message}</p>}
//             </form>
//         </div>
//     );
// }
return (
    <div className={styles.container}>
        {!songDetails ? (
            <div>
                <h1 className={styles.title}>Create A New Song Inspo</h1>
                <form onSubmit={handleSubmit} className={styles.form}>
                  <div className={styles.row}>
                    <div className={styles.inputField}>
                        <label>Genre</label>
                        <select className={styles.select} value={selectedGenre} onChange={e => setSelectedGenre(e.target.value)}>
                            {genres.map(genre => (
                                <option key={genre.id} value={genre.name}>{genre.name}</option>
                            ))}
                        </select>
                    </div>
                    <div className={styles.inputField}>
                        <label>Dancability</label>
                        <select className={styles.select} value={dancability} onChange={e => setDancability(e.target.value)}>
                            <option value="1">Not Danceable</option>
                            <option value="2">slightly Danceable</option>
                            <option value="3">Very Danceable</option>
                        </select>
                    </div>
                    <div className={styles.inputField}>
                        <label>Title</label>
                        <input type="text" className={styles.input} value={title} onChange={e => setTitle(e.target.value)} />
                    </div>
                    </div>  
                    <button type="submit" className={styles.button}>Create Song</button>
                </form>
                {message && <p className={styles.message}>{message}</p>}
            </div>
        ) : (
            <div className={styles.container}>
            <h2 className={styles.header}>Your Creation</h2>
            <div className={styles.songDetails}>
                <p className={styles.detail}><strong>Title:</strong> {songDetails.Title}</p>
                <p className={styles.detail}><strong>Dancability:</strong> {songDetails.Dancability}</p>
                <p className={styles.detail}><strong>Artist:</strong> {songDetails.Artist}</p>
                <p className={styles.detail}><strong>Lyrics:</strong> {songDetails.Lyrics}</p>
                <p className={styles.detail}><strong>Creation Date:</strong> {songDetails.Creation_Date}</p>
                <p className={styles.detail}><strong>Released Status:</strong> {songDetails.Released_Status}</p>
                <p className={styles.detail}><strong>Time Signature:</strong> {songDetails.Time_Signature}</p>
            </div>
            <div className={styles.instruments}>
                {songDetails.instruments.map((instrument, index) => (
                    <div key={index} className={styles.instrumentDetail}>
                        <p>Name: {instrument.name}</p>
                        <p>Ethnic Influence: {instrument.ethnic_influence}</p>
                        <p>Chord Progression: {instrument.chord_progression}</p>
                    </div>
                ))}
            </div>
            <button className={styles.editButton} onClick={() => setSongDetails(null)}>Edit creation</button>
        </div>
        )}
    </div>
);
}