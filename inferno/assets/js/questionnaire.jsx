var React = require('react')

export default class Questionnaire extends React.Component{
  render() {
    return(
      <div className="ui small basic test modal">
        <div className="ui icon header">
          <i className="archive icon"></i>
            {'評比問卷'}
        </div>
        <div className="content">
          <div className="ui form">
            <div className="ui icon header">
              <div className="ui blue ribbon label">
                <div className="">點名扣分：</div> 扣分<div className="ui star rating" data-rating="3" data-max-rating="5"></div>不扣
              </div>
              <div className="ui blue ribbon label">
                <div className="">點名次數：</div> 很多<div className="ui star rating" data-rating="3" data-max-rating="5"></div>很少
              </div>
              <div className="ui blue ribbon label">
                <div className="">我的分數：</div> 很低<div className="ui star rating" data-rating="3" data-max-rating="5"></div>很高
              </div>
              <div className="ui blue ribbon label">
                <div className="">考試多寡：</div> 很多<div className="ui star rating" data-rating="3" data-max-rating="5"></div>很少
              </div>
              <div className="ui blue ribbon label">
                <div className="">考試難度：</div> 困難<div className="ui star rating" data-rating="3" data-max-rating="5"></div>簡單
              </div>
              <div className="ui blue ribbon label">
                <div className="">上課氛圍：</div>  安靜<div className="ui star rating" data-rating="3" data-max-rating="5"></div>活潑
              </div>
              <div className="ui blue ribbon label">
                <div className="">知識性：</div> 很少<div className="ui star rating" data-rating="3" data-max-rating="5"></div>很多 
              </div>
              <div className="ui blue ribbon label">
                <div className="">輕鬆度：</div> 很硬<div className="ui star rating" data-rating="3" data-max-rating="5"></div>輕鬆
              </div>
              <div className="ui blue ribbon label">
                <div className="">作業量：</div> 很多<div className="ui star rating" data-rating="3" data-max-rating="5"></div>很少
              </div>
            </div>
          </div>
        </div>
        <div className="actions">
          <div className="ui red basic cancel inverted button">
            <i className="remove icon"></i>
            取消
          </div>
          <div className="ui green ok inverted button" id="questionnaire">
            <i className="checkmark icon botton"></i>
            提交
          </div>
        </div>
      </div>

    )
  }
}