import React, { useEffect, useState } from 'react';
import axios from 'axios';
import StoryList from './components/StoryList';
import Loading from './components/Loading';
import './App.css';

const App = () => {
    const [stories, setStories] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchStories = async () => {
            try {
                const response = await axios.get(`${process.env.REACT_APP_BACKEND_URL}/top-stories`);
                setStories(response.data);
            } catch (error) {
                setError('Error fetching stories');
            } finally {
                setLoading(false);
            }
        };
        fetchStories();
    }, []);

    if (loading) return <Loading />;
    if (error) return <div>{error}</div>;

    return (
        <div className="App">
            <h1>Top 10 Hacker News Stories</h1>
            <StoryList stories={stories} />
        </div>
    );
};

export default App;
