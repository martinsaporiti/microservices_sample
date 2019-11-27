import React, {useEffect, useState} from 'react';

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
        <div>
            {obra.name} - {rating}
        </div>
    );
};


export default Obra;