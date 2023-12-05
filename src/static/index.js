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