import React from 'react';
import { render, screen } from '@testing-library/react';
import App from '../App';

test('renders loading message initially', () => {
    render(<App />);
    const loadingElement = screen.getByText(/Loading stories/i);
    expect(loadingElement).toBeInTheDocument();
});
