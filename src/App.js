import './App.css';
import Header from './Header';
import Footer from './Footer';
import Statistique from './Statistique';

function App() {
  return (
    <div className="App">
      <Header />
      <main className="contenu">
        <p>Bienvenue ! Cette application vous aide à trouver votre ligne de bus à Dakar.</p>

        <div style={{ display: 'flex', justifyContent: 'center', flexWrap: 'wrap' }}>
          <Statistique chiffre="37" libelle="Lignes de bus" />
          <Statistique chiffre="500+" libelle="Arrêts desservis" />
          <Statistique chiffre="3" libelle="Compagnies partenaires" />
        </div>
      </main>
      <Footer />
    </div>
  );
}

export default App;