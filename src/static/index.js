function toggle_bibtex(viite_id) {
    let bibtex_div = document.getElementById('wrapperi_' + viite_id);
    let nappi = document.getElementById('bibtex_nappi_' + viite_id);
    if(nappi.textContent == "Näytä BibTex") {
        näytä_bibtex(viite_id, bibtex_div, nappi);
    } else {
        piilota_bibtex(viite_id, bibtex_div, nappi);
    }
}

function näytä_bibtex(viite_id, bibtex_div, nappi) {
    nappi.textContent = "Piilota BibTex";
    bibtex_div.style.display = "block";
}

function piilota_bibtex(viite_id, bibtex_div, nappi) {
    nappi.textContent = "Näytä BibTex";
    bibtex_div.style.display = "none";
}

function toggleForm(formName) {
    var kirjaForm = document.getElementById('kirjaForm');
    var artikkeliForm = document.getElementById('artikkeliForm');
    var kirjaButton = document.getElementById('kirjaButton');
    var artikkeliButton = document.getElementById('artikkeliButton');
    var kirjaHeading = document.getElementById('kirjaHeading');
    var artikkeliHeading = document.getElementById('artikkeliHeading');
    var kaikkiButton = document.getElementById('kaikkiButton');

    if (formName === 'kirja') {
        kirjaForm.classList.remove('hidden');
        kirjaButton.classList.add('active-button');
        kirjaHeading.classList.remove('hidden');
        artikkeliForm.classList.add('hidden');
        artikkeliButton.classList.remove('active-button');
        artikkeliHeading.classList.add('hidden');
        kaikkiButton.classList.remove('active-button');
    } else if (formName === 'artikkeli') {
        kirjaForm.classList.add('hidden');
        kirjaButton.classList.remove('active-button');
        kirjaHeading.classList.add('hidden');
        artikkeliForm.classList.remove('hidden');
        artikkeliButton.classList.add('active-button');
        artikkeliHeading.classList.remove('hidden');
        kaikkiButton.classList.remove('active-button');
    } else if (formName === 'kaikki') {
        kaikkiButton.classList.add('active-button');
        kirjaForm.classList.remove('hidden');
        kirjaButton.classList.remove('active-button');
        kirjaHeading.classList.remove('hidden');
        artikkeliForm.classList.remove('hidden');
        artikkeliButton.classList.remove('active-button');
        artikkeliHeading.classList.remove('hidden');
    }
}

function toggleShown(formName) {
    var kaikkiKirjatButton = document.getElementById('kaikkiKirjaViitteetButton');
    var kaikkiArtikkeliViitteetButton = document.getElementById('kaikkiArtikkeliViitteetButton');
    var kaikkiViitteetButton = document.getElementById('kaikkiViitteetButton');
    var kaikkiContainer = document.getElementById('kaikkiViitteetContainer');
    var kirjatContainer = document.getElementById('kirjaViitteetContainer');
    var artikkeliContainer = document.getElementById('artikkeliViitteetContainer');
    var poistaKaikkiTeksti = document.getElementById('poistaKaikkiTeksti');
    var poistaKirjatTeksti = document.getElementById('poistaKirjatTeksti');
    var poistaArtikkelitTeksti = document.getElementById('poistaArtikkelitTeksti');

    if (formName === 'kirja') {
        kaikkiKirjatButton.classList.add('active-button');
        kaikkiArtikkeliViitteetButton.classList.remove('active-button');
        kaikkiViitteetButton.classList.remove('active-button');
        kaikkiContainer.classList.add('hidden');
        kirjatContainer.classList.remove('hidden');
        artikkeliContainer.classList.add('hidden');
        poistaKaikkiTeksti.classList.add('hidden');
        poistaKirjatTeksti.classList.remove('hidden');
        poistaArtikkelitTeksti.classList.add('hidden');
    } else if (formName === 'artikkeli') {
        kaikkiKirjatButton.classList.remove('active-button');
        kaikkiArtikkeliViitteetButton.classList.add('active-button');
        kaikkiViitteetButton.classList.remove('active-button');
        kaikkiContainer.classList.add('hidden');
        kirjatContainer.classList.add('hidden');
        artikkeliContainer.classList.remove('hidden');
        poistaKaikkiTeksti.classList.add('hidden');
        poistaKirjatTeksti.classList.add('hidden');
        poistaArtikkelitTeksti.classList.remove('hidden');
    } else if (formName === 'kaikki') {
        kaikkiKirjatButton.classList.remove('active-button');
        kaikkiArtikkeliViitteetButton.classList.remove('active-button');
        kaikkiViitteetButton.classList.add('active-button');
        kaikkiContainer.classList.remove('hidden');
        kirjatContainer.classList.add('hidden');
        artikkeliContainer.classList.add('hidden');
        poistaKaikkiTeksti.classList.remove('hidden');
        poistaKirjatTeksti.classList.add('hidden');
        poistaArtikkelitTeksti.classList.add('hidden');
    }
}

