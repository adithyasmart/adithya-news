import React from 'react';

const StoryList = ({ stories }) => {
    return (
        <ul>
            {stories.map((story, index) => (
                <li key={index}>
                    <a href={story.url} target="_blank" rel="noopener noreferrer">{story.title}</a>
                    <p>Author: {story.author}</p>
                    <p>Score: {story.score}</p>
                    <p>Created At: {story.time}</p>
                </li>
            ))}
        </ul>
    );
};

export default StoryList;
