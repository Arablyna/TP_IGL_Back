import React from "react";
import { useState, useEffect } from "react";
import {IoFilterOutline, IoAddOutline} from "react-icons/io5";
import AnnonceCard from "../../Components/AnnonceCard";
import NavBar from "./NavBar";
import AnnonceDetailsCard from './AnnonceDétailsCard.jsx'
import FiltresCard from './FiltresCard.jsx'
import AddCard from "./AddCard.jsx";
import {useSelector} from 'react-redux';
import '../../App.css';

const AnnoncesPage = () => {
  const user = useSelector((state) => state.user.value);
  const annonces = [
    {
      "Poster": ["https://images.adsttc.com/media/images/5efe/1f7f/b357/6540/5400/01d7/newsletter/archdaily-houses-104.jpg?1593712501", "https://uploads-ssl.webflow.com/5fa8df3ac2183ee78c7be185/5fb2f73a910d32a62244aaa4_hero_optimized.webp"],
      "Price": "110 000 000",
      "Infos": "5 bed   |   4 bath   |   2 backyard   |   270 m2",
      "Location": "Oued Smar, Alger",
      "Date" : "15 décembre 2022",
    },
    {
      "Poster": ["https://uploads-ssl.webflow.com/5fa8df3ac2183ee78c7be185/5fb2f73a910d32a62244aaa4_hero_optimized.webp"],
      "Price": "110 000 000",
      "Infos": "5 bed   |   4 bath   |   2 backyard   |   270 m2",
      "Location": "Oued Smar, Alger",
      "Date" : "15 décembre 2022",
    },
    {
      "Poster": ["https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg?cs=srgb&dl=pexels-vecislavas-popa-1571460.jpg&fm=jpg", "https://images.adsttc.com/media/images/5efe/1f7f/b357/6540/5400/01d7/newsletter/archdaily-houses-104.jpg?1593712501", "https://uploads-ssl.webflow.com/5fa8df3ac2183ee78c7be185/5fb2f73a910d32a62244aaa4_hero_optimized.webp"],
      "Price": "110 000 000",
      "Infos": "5 bed   |   4 bath   |   2 backyard   |   270 m2",
      "Location": "Oued Smar, Alger",
      "Date" : "15 décembre 2022",
    },
    {
      "Poster": ["https://images.adsttc.com/media/images/5f2c/8545/b357/65db/c000/008c/large_jpg/FEAT_ID.jpg?1596753213", "https://uploads-ssl.webflow.com/5fa8df3ac2183ee78c7be185/5fb2f73a910d32a62244aaa4_hero_optimized.webp"],
      "Price": "110 000 000",
      "Infos": "5 bed   |   4 bath   |   2 backyard   |   270 m2",
      "Location": "Oued Smar, Alger",
      "Date" : "15 décembre 2022",
    },
    {
      "Poster": ["https://images.adsttc.com/media/images/5efe/1f7f/b357/6540/5400/01d7/newsletter/archdaily-houses-104.jpg?1593712501", "https://uploads-ssl.webflow.com/5fa8df3ac2183ee78c7be185/5fb2f73a910d32a62244aaa4_hero_optimized.webp"],
      "Price": "120 000 000",
      "Infos": "5 bed   |   4 bath   |   2 backyard   |   270 m2",
      "Location": "Oued Smar, Alger",
      "Date" : "15 décembre 2022",
    },
    {
      "Poster": ["https://uploads-ssl.webflow.com/5fa8df3ac2183ee78c7be185/5fb2f73a910d32a62244aaa4_hero_optimized.webp"],
      "Price": "110 000 000",
      "Infos": "5 bed   |   4 bath   |   2 backyard   |   270 m2",
      "Location": "Oued Smar, Alger",
      "Date" : "15 décembre 2022",
    },
    {
      "Poster": ["https://images.adsttc.com/media/images/5efe/1f7f/b357/6540/5400/01d7/newsletter/archdaily-houses-104.jpg?1593712501", "https://uploads-ssl.webflow.com/5fa8df3ac2183ee78c7be185/5fb2f73a910d32a62244aaa4_hero_optimized.webp"],
      "Price": "110 000 000",
      "Infos": "5 bed   |   4 bath   |   2 backyard   |   270 m2",
      "Location": "Oued Smar, Alger",
      "Date" : "15 décembre 2022",
    },
    {
      "Poster": ["https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg?cs=srgb&dl=pexels-vecislavas-popa-1571460.jpg&fm=jpg", "https://images.adsttc.com/media/images/5efe/1f7f/b357/6540/5400/01d7/newsletter/archdaily-houses-104.jpg?1593712501", "https://uploads-ssl.webflow.com/5fa8df3ac2183ee78c7be185/5fb2f73a910d32a62244aaa4_hero_optimized.webp"],
      "Price": "110 000 000",
      "Infos": "5 bed   |   4 bath   |   2 backyard   |   270 m2",
      "Location": "Oued Smar, Alger",
      "Date" : "15 décembre 2022",
    },
  ];

  // useEffect(() => {
  //   fetch("http://127.0.0.1:8000/homes/annonce/")
  //   .then(response => response.json())
  //   .then(data => console.log(data))
  //   .catch(error => console.error(error));
  // }, []);

  const [openDetails, setOpenDetails] = useState(false)
  const [openFiltres, setOpenFiltres] = useState(false)
  const [openAjout, setOpenAjout] = useState(false)
  const [selectedAnnonce, setSelectedAnnonce] = useState({})
  return (
    <div className="annoncesPage">
      <div className="background">
        <NavBar/>
        <div className="results">
          <div className="bar">
          <h1>Annonces immobilières</h1> 
          <div className="buttons">
            <button onClick={() => {setOpenFiltres(true)}}>Filtres<IoFilterOutline/></button>
            <button id="publier" onClick={() => {setOpenAjout(true)}}>Publier<IoAddOutline/></button>
          </div>
          </div>

          {
            annonces.length > 0 ?
            (
                <div className="AllAnnonces">
                    {
                      annonces.map((annonce) => (
                        <button className="grid" onClick={() => {setOpenDetails(true); setSelectedAnnonce(annonce) }}><AnnonceCard annonce={annonce}/></button>
                      ))
                    }
                </div>
            ) :
            (
                <div className="empty">
                    <h2>Aucune annonce trouvée</h2>
                </div>
            )
          }
        </div>
      </div>
      {
        openDetails && <AnnonceDetailsCard annonce = {selectedAnnonce} closeDetails={setOpenDetails}/>
      }
      {
        openFiltres && <FiltresCard closeFiltres={setOpenFiltres}/>
      }
      {
        openAjout && <AddCard closeAjout={setOpenAjout}/>
      }
    </div>
  );
}

export default AnnoncesPage;
