fetch("https://hellosalut.stefanbohacek.dev/?lang=es")
    .then(response => response.json())
    .then(data => {
      document.getElementById('hello').textContent = data.hello;
    })
    .catch(error => console.error('Error fetching translation:', error));
