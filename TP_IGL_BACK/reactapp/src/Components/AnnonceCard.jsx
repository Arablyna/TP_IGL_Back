import React from "react";

const AnnonceCard = ({annonce}) => {
    return (
        <div className="annonce">
            <div>
                <img src={annonce.Poster.length > 0 ? annonce.Poster[0] : 'https://via.placeholder.com/400'}
                    alt='Annonce Poster'/>
            </div>
            <div className="infos">
                <div className="smallInfos">
                    <h2>{annonce.Price} DA</h2>
                    <h3>{annonce.Infos}</h3>
                </div>
                <div>
                    <h3>{annonce.Location}</h3>
                </div>
            </div>
        </div>
    )
}
export default AnnonceCard;