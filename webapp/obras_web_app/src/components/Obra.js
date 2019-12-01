import React, {useEffect, useState} from 'react';
import ObraList from './ObraList';

const Obra = ({obra}) => {

    const [rating, setRating] = useState('');
    
    useEffect( () =>{

        const consultarApi = async () => {

            const url = (window.REACT_APP_RATINGS_API_URL != undefined) 
                ? window.REACT_APP_RATINGS_API_URL + obra.id
                : `${process.env.REACT_APP_RATINGS_API_URL}${obra.id}`
            
            // const url = `${process.env.REACT_APP_RATINGS_API_URL}${obra.id}`;
        
            // Conultar la URL
            const respuesta = await fetch(url);
            const resultado = await respuesta.json();
            console.log(resultado);
            setRating(resultado.rating);
        }

        consultarApi();

    }, [])

    return (

        <div className="card border-secondary mb-3">
            <div className="card-header">{obra.name}</div>
            <div className="card-body">
            <h4 className="card-title">{obra.artist}</h4>
            <p className="card-text">Rating: {rating}</p>
            <p className="card-text">Price: ${obra.price}</p>
            </div>
            <img src={obra.img} className="card-img-top"></img>
            <button type="button" class="btn btn-primary btn-sm button-card">Buy</button>
        </div>
    );
};


export default Obra;