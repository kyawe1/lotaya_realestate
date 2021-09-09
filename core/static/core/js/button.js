m = document.getElementsByClassName('btn btn-primary w-100')
for (i of m) {

    i.onclick = (e) => {
        
        if (e.target.tagName == 'BUTTON') {
            // console.log(e)
            // console.log(e.target.children[0].className)
            if (e.target.children[0].className == 'bi bi-star-fill mx-2') {
                e.target.children[0].className = 'bi bi-star mx-2'
            } else {
                e.target.children[0].className = 'bi bi-star-fill mx-2'
            }
        }
        

    }
}
k = document.getElementsByName('btn-icon')
for (i of k) {
    i.onclick = (e) => {
        if (e.target.className == 'bi bi-star-fill mx-2') {
            e.target.className = 'bi bi-star mx-2'
        } else {
            e.target.className = 'bi bi-star-fill mx-2'
        }

    }
}