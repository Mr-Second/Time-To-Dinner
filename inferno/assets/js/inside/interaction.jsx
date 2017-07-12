var React = require('react')

const Interaction = () => {
  const showQuestionnaire = () => {
    if(window.res['id']==undefined){
        toastr.error('請登入後再參與評分')
        return
    }
    $('.rating').rating('setting', 'clearable', true);// make questionnaire rating star clearable.
    $('.modal')
      .modal('show')
    ;
    return          
  }
  return(
    <button className="ui primary button" id="goquestion" onClick={showQuestionnaire}>參與評比該課程</button>
  )
}
export default Interaction