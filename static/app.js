




  

  // This changes the text in the search bar to the selection from autocomplete
  function onPlaceChanged(){
      var place = autocomplete.getPlace();

      if(!place.geometry){
          document.getElementById('autocomplete').placeholder = 'Enter a place';
      }
      else {
          document.getElementById('details').innerHTML = place.name;
      }
  }


//   const toggleMarkerDescrip = () => {
//       document.querySelector('.descrip_modal')
//         .classList.toggle('descrip_modal--hidden');
//   };

//   document.querySelector()
  
//get modal element
var modal = document.getElementById('locationModal');
var modalBtn = document.getElementById('modalBtn');
var closeBtn = document.getElementsByClassName('closeBtn')[0];

modalBtn.addEventListener('click',openModal);
closeBtn.addEventListener('click',closeModal);
window.addEventListener('click',clickOutside);
//open modal
function openModal(){
    modal.style.display = 'block';
}

//close modal

function closeModal(){
    modal.style.display = 'none';
}

function clickOutside(e){
    if(e.target == modal){
        modal.style.display = 'none';
    }
}

