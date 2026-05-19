import './Recherche.css';

function Recherche({ valeur, onChange, onClear }) {
  return (
    <div className="recherche">
      <input
        type="text"
        className="recherche-input"
        placeholder="Rechercher une ligne (depart, arrivee)..."
        value={valeur}
        onChange={e => onChange(e.target.value)}
      />
      <button className="recherche-clear" onClick={onClear}>
        Effacer
      </button>
    </div>
  );
}

export default Recherche;