Vue.component('com-img-group',{
    props:['frontImg'],
    template:`<div >
            <img src="/static/home/1_1.png" alt="" style="position: absolute;top:0;left:0;"/>
            <img src="/static/home/1_2.png" alt="" style="position: absolute;top:20px;left:0;"/>
            <img :src="frontImg" alt="" style="position: absolute;top:20px;left:-10px;"/>
             <slot></slot>
        </div>`,

})
///static/home/2.png