// import React, { useState } from 'react';
// import { useRouter } from 'next/router';


// function Login() {
//     const [username, setUsername] = useState('');
//     const [password, setPassword] = useState('');
//     const [message, setMessage] = useState('');
//     const router = useRouter();

//     const handleSubmit = async (event) => {
//         event.preventDefault();
//         try {
//             const response = await fetch('http://127.0.0.1:5000/api/login', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                 },
//                 body: JSON.stringify({ username, password })
//             });
//             const data = await response.json();
//             if (response.ok) {
//                 localStorage.setItem('token', data.access_token);  // Ensure you are setting the correct property
//                 setMessage('Login successful');
//                 router.push('/create_song');
//             } else {
//                 setMessage(data.msg || 'Login failed');
//             }
//         } catch (error) {
//             console.error('Login error:', error);
//             setMessage('Network error');
//         }
//     };

//     return (
//         <div>
//             <h1>Login</h1>
//             <form onSubmit={handleSubmit}>
//                 <label>
//                     Username:
//                     <input type="text" value={username} onChange={e => setUsername(e.target.value)} />
//                 </label>
//                 <label>
//                     Password:
//                     <input type="password" value={password} onChange={e => setPassword(e.target.value)} />
//                 </label>
//                 <button type="submit">Login</button>
//             </form>
//             {message && <p>{message}</p>}
//         </div>
//     );
// }

import React, { useState } from 'react';
import { useRouter } from 'next/router';
import styles from './Login.module.css';  // correct import of CSS module

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');
    const router = useRouter();

    const handleSubmit = async (event) => {
        event.preventDefault();
        event.preventDefault();
            try {
                const response = await fetch('http://127.0.0.1:5000/api/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ username, password })
                });
                const data = await response.json();
                if (response.ok) {
                    localStorage.setItem('token', data.access_token);  // Ensure you are setting the correct property
                    setMessage('Login successful');
                    router.push('/create_song');
                } else {
                    setMessage(data.msg || 'Login failed');
                }
            } catch (error) {
                console.error('Login error:', error);
                setMessage('Network error');
            }
        };
    

    return (
        <div className={styles.container}>
            <form onSubmit={handleSubmit} className={styles.form}>
                <h1 className={styles.title}>Song Maker</h1>
                <div className={styles.inputField}>
                    <label>Username:</label>
                    <input
                        type="text"
                        value={username}
                        onChange={e => setUsername(e.target.value)}
                        className={styles.input}
                    />
                </div>
                <div className={styles.inputField}>
                    <label>Password:</label>
                    <input
                        type="password"
                        value={password}
                        onChange={e => setPassword(e.target.value)}
                        className={styles.input}
                    />
                </div>
                <button type="submit" className={styles.button}>Login</button>
                {message && <p className={styles.message}>{message}</p>}
            </form>
        </div>
    );
}

export default Login;
