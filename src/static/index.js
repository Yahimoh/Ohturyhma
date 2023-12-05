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