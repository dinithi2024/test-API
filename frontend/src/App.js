import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [destinations, setDestinations] = useState([]);

  useEffect(() => {
    // Fetch data from the Flask API
    axios.get('http://127.0.0.1:5000/api/destinations')
      .then(response => {
        setDestinations(response.data); // Store data in state
      })
      .catch(error => {
        console.error('Error fetching data:', error); // Handle error
      });
  }, []);

  return (
    <div className="App">
      <h1>Travel Destinations</h1>
      <ul>
        {destinations.map(destination => (
          <li key={destination.id}>{destination.name} - {destination.country}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
