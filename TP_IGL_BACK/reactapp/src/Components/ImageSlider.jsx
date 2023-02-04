import React from "react";
import Carousel from "react-elastic-carousel";

const ImageSlider = ({ImageList}) => {
    return(
        <div className="Carousel">
            <Carousel >
                {
                    ImageList.map((image) =>(
                        <img src={image} alt={image}/>
                    ))
                }
            </Carousel>
        </div>
    );
}
export default ImageSlider;