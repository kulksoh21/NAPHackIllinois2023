document.getElementById("search").addEventListener("click", () => {
    response = fetch("http://localhost:5000", 
    {method: "GET"})
    const resJson = response;
    if (resJson.status === 201) {
      JSON.stringify(response)
    }
    //initializations
    let searchInput = document.getElementById("search-input").value;
    let elements = document.querySelectorAll(".product-name");
    let cards = document.querySelectorAll(".card");
    //loop through all elements
    elements.forEach((element, index) => {
      //check if text includes the search value
      if (element.innerText.includes(searchInput.toUpperCase())) {
        //display matching card
        cards[index].classList.remove("hide");
      } else {
        //hide others
        cards[index].classList.add("hide");
      }
    });
  });