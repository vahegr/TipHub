function like(id, slug){
    var element = document.getElementById("like")
    var count = document.getElementById("count")
    $.get(`/videos/video_like/${id}/${slug}`).then(response =>{
        if(response['response'] === "unliked"){
            element.className = "fa fa-heart-o"
            count.innerText = Number(count.innerText) - 1
        }
        else{
            element.className = "fa fa-heart liked"
            count.innerText = Number(count.innerText) + 1
        }
    })
}