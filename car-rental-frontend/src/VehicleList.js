import React, { useEffect, useState } from 'react';
import axios from 'axios';


function VehicleList(){
	const [vehicles, setVehicles] = useState([]);

	useEffect(() => {
		axios.get('http://localhost:8000/vehicles/')
		.then(response => setVehicles(response.data))
		.catch(error => console.log(error));

	}, []);

	return (
		<div>

		   <h1>Vehicles</h1>
		   <ul>
		     {vehicles.map(vehicle => (
			     <li key={vehicle.id}>
			       <img src={vehicle.image} alt={vehicle.name} style={{width: "200"}} />
			     <div>
			         <h2>{vehicle.name}</h2>
			         <p> {vehicle.vehicle_type} - ${vehicle.daily_rate}/day</p>
			     	 <p> {vehicle.description}</p>
			     </div>
			     </li>
		     ))}
		   </ul>
		</div>


	);

    }


export default VehicleList;


