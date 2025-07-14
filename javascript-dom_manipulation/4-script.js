document.querySelector('#add_item').addEventListener('click', function() {
    const newItem = document.createElement('li');
    newItem.textContent = 'item';
    document.querySelector('.my_list').appendChild(newItem);
})