var React = require('react')
import Profile from './profile.jsx'
import Questionnaire from './questionnaire.jsx'
const Information = () => {
  return(
    <div className="ten wide column">
      <Profile/>
      <hr className="fade"/>
      <Questionnaire/>          
    </div>
  )
}
export default Information;