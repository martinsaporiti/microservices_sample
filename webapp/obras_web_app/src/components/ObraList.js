import React,{useEffect, useState} from 'react';
import Obra from './Obra';


const ObraList = () => {

    const [obras, setObras] = useState([]);
    
    
    useEffect( () =>{

        const consultarApi = async () => {
            const url = (window.REACT_APP_OBRAS_API_URL != undefined) 
                ? window.REACT_APP_OBRAS_API_URL + 'obras' 
                : `${process.env.REACT_APP_OBRAS_API_URL}obras`
            // const url = `${process.env.REACT_APP_OBRAS_API_URL}obras`;
            console.log(url);
            // Conultar la URL
            const respuesta = await fetch(url);
            const resultado = await respuesta.json();
            console.log(resultado);
            setObras(resultado);
        }

        consultarApi();

    }, [])

    return (
        <div>
            { obras.map( (obra) => (
                
                <Obra
                    key = {obra.id}
                    obra = {obra}
                />
            ))}
        </div>
    );
};

export default ObraList;