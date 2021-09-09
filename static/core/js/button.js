createdata = (id) => {
    $.ajax(
        {
            url: '/interest/create',
            method: 'get',
            data: {
                'p_id': id
            },
            success: () => {
                console.log('mm')
            },
            error: () => {
                console.error('not good')
            }
        }
    )
}
deleteapi = (id) => {
    $.ajax(
        {
            url: '/interest/delete',
            method: 'get',
            data: {
                'p_id': id
            },
            success: () => {
                console.log('mm')
            },
            error: () => {
                console.error('not good')
            }
        }
    )
}

m = document.getElementsByClassName('btn btn-primary w-100')
for (i of m) {

    i.onclick = (e) => {
        
        if (e.currentTarget.tagName == 'BUTTON') {
            
            if (e.currentTarget.children[0].className == 'bi bi-star-fill mx-2') {
                deleteapi(e.currentTarget.value)
                e.currentTarget.children[0].className = 'bi bi-star mx-2'
            } else {
                createdata(e.currentTarget.value)
                e.currentTarget.children[0].className = 'bi bi-star-fill mx-2'
            }
        }
        

    }
}
// k = document.getElementsByName('btn-icon')
// for (i of k) {
//     i.onclick = (e) => {
//         console.log(e.currentTarget)
//         if (e.target.className == 'bi bi-star-fill mx-2') {
//             console.log(e.currenttarget)
//             e.target.className = 'bi bi-star mx-2'
//         } else {
//             e.target.className = 'bi bi-star-fill mx-2'
//         }

//     }
// }