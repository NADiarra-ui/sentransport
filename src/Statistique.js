import './Statistique.css';

function Statistique(props) {
  return (
    <div className="statistique">
      <span className="statistique-chiffre">{props.chiffre}</span>
      <span className="statistique-libelle">{props.libelle}</span>
    </div>
  );
}

export default Statistique;