import React from "react";
import * as Components from './Components';
import { useState, useEffect } from "react";
import jwt_decode from "jwt-decode";
import useSelector from "react-redux";

const AuthPage = () => {
    const [user, setUser] = useState({});
    // const currentUser = useSelector({state}) => state.user.value);

    const handleCallBackResponse = (response) => {
        var userObject = jwt_decode(response.credential);
        const userInfos = {
            "nom" : userObject["family_name"],
            "prenom" : userObject["given_name"],
            "email" : userObject["email"],
            "photo" : userObject["picture"]
        }
        setUser(userInfos);
        document.getElementById("Signin").hidden = true;
    }

    const handleSignOut = (e) => {
        setUser({});
        document.getElementById("Signin").hidden = false;
    }

    useEffect(() => {
        // console.log("check user");
        // console.log(state.count.value);
        /*global google*/
        google.accounts.id.initialize({
            client_id : "64942602411-9c3v2baidusqrppj68cmc43v66pp1a0k.apps.googleusercontent.com",
            callback : handleCallBackResponse
        });

        google.accounts.id.renderButton(
            document.getElementById("Signin"),
            {theme : "outline", size: "large"}
        );

        google.accounts.id.prompt();
    }, []);

    const [signIn, toggle] = React.useState(true);
     return(
        <div className="App">
            <div id="Signin"></div>
            {
                Object.keys(user).length != 0 &&
                <button onClick={(e) => handleSignOut(e)}>Sign Out</button>
            }
            
            {
                user &&
                <div>
                    <img src={user.photo}></img>
                    <h3>{user.nom}</h3>
                </div>
            }
        </div>
        //  <Components.Container>
        //      <Components.SignUpContainer signinIn={signIn}>
        //          <Components.Form>
        //              <Components.Title>Creer un compte</Components.Title>
        //              <Components.Input type='text' placeholder='Nom complet' />
        //              <Components.Input type='email' placeholder='Email' />
        //              <Components.Input type='password' placeholder='Mot de passe' />
        //              <Components.Button>S'inscrire'</Components.Button>
        //          </Components.Form>
        //      </Components.SignUpContainer>

        //      <Components.SignInContainer signinIn={signIn}>
        //           <Components.Form>
        //               <Components.Title>Se connecter</Components.Title>
        //               <Components.Input type='email' placeholder='Email' />
        //               <Components.Input type='password' placeholder='Mot de passe' />
        //               <Components.Anchor href='#'>Se connecter avec Gmail</Components.Anchor>
        //               <Components.Button>Se connecter</Components.Button>
        //           </Components.Form>
        //      </Components.SignInContainer>

        //      <Components.OverlayContainer signinIn={signIn}>
        //          <Components.Overlay signinIn={signIn}>

        //          <Components.LeftOverlayPanel signinIn={signIn}>
        //              <Components.Title>Connecter maintenant!</Components.Title>
        //              <Components.Paragraph>
        //                  Connecter avec votre compte sokna
        //              </Components.Paragraph>
        //              <Components.GhostButton onClick={() => toggle(true)}>
        //                  Se connecter 
        //              </Components.GhostButton>
        //              </Components.LeftOverlayPanel>

        //              <Components.RightOverlayPanel signinIn={signIn}>
        //                <Components.Title>Sokna</Components.Title>
        //                <Components.Paragraph>
        //                Publier et consulter les annonces immobilières avec Sokna .
        //                </Components.Paragraph>
        //                    <Components.GhostButton onClick={() => toggle(false)}>
        //                      S'inscrire
        //                    </Components.GhostButton> 
        //              </Components.RightOverlayPanel>
 
        //          </Components.Overlay>
        //      </Components.OverlayContainer>

        //  </Components.Container>
     )
}
export default AuthPage;
