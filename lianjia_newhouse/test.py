from bs4 import BeautifulSoup
html = """<ul class="resblock-list-wrapper">
            
                
                
            
                        <li class="resblock-list post_ulog_exposure_scroll has-results" data-project-name="bgyfhgjggafscm" data-ulog-exposure="xinfangpc_show=20005&amp;location=1&amp;project_name=bgyfhgjggafscm&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268416&quot;,&quot;fb_item_location&quot;:&quot;0&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100112&quot;}" has_been_exposed="1">
                <a href="/loupan/p_bgyfhgjggafscm/" class="resblock-img-wrapper " title="碧桂园凤凰国际公馆" data-xftrack="10138" data-other-action="location=1&amp;project_name=bgyfhgjggafscm&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268416&quot;,&quot;fb_item_location&quot;:&quot;0&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100112&quot;}" target="_blank" data-source-type="recommend_projectlist" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268416&quot;,&quot;fb_item_location&quot;:&quot;0&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100112&quot;}">
                    <img alt="碧桂园凤凰国际公馆楼盘图片" class="lj-lazy" data-original="https://image1.ljcdn.com/hdic-resblock/02b3fdfe-5437-45ec-95a6-978e0729bf7c.png.592x432.jpg" src="https://image1.ljcdn.com/hdic-resblock/02b3fdfe-5437-45ec-95a6-978e0729bf7c.png.592x432.jpg" style="display: inline;">
                    <ul class="icon-wrapper">
                        
                        
                            
                            
                        
                        
                        
                            
                                
                                
                            
                        
                        
                            
                                
                                
                            
                        
                                            </ul>
                                        <div class="discount">砸金蛋</div>
                    
                    <div class="watermark">效果图</div>
                </a>
                <div class="resblock-desc-wrapper">
                    <div class="resblock-name">
                        <a href="/loupan/p_bgyfhgjggafscm/" class="name " target="_blank" data-xftrack="10138" data-other-action="location=1&amp;project_name=bgyfhgjggafscm&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268416&quot;,&quot;fb_item_location&quot;:&quot;0&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100112&quot;}" data-source-type="recommend_projectlist" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268416&quot;,&quot;fb_item_location&quot;:&quot;0&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100112&quot;}">碧桂园凤凰国际公馆</a>
                        <span class="resblock-type" style="background: #FB9252;">住宅</span>
                        <span class="sale-status" style="background: #53CC9A;">在售</span>
                    </div>
                    <div class="resblock-location">
                        <span>坪山区</span>
                        <i class="split"> /</i>
                        <span> 坪山</span>
                        <i class="split"> / </i>
                        <a href="/loupan/p_bgyfhgjggafscm/#around" target="_blank" data-xftrack="10254" data-other-action="strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268416&quot;,&quot;fb_item_location&quot;:&quot;0&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100112&quot;}">碧沙北路以西、龙勤路以南</a>
                    </div>
                    <a class="resblock-room" href="/loupan/p_bgyfhgjggafscm/#house-online" data-xftrack="10255" target="_blank" data-other-action="strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268416&quot;,&quot;fb_item_location&quot;:&quot;0&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100112&quot;}" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268416&quot;,&quot;fb_item_location&quot;:&quot;0&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100112&quot;}">
                                                    <span> 3 室</span>
                                                            <i class="split"> /</i>
                                                                                <span>4 室</span>
                                                    
                    </a>
                    <div class="resblock-area">
                        <span>建面 65-120㎡</span>
                    </div>
                    <div class="resblock-agent"><span class="agent">新房顾问：黄奎号</span>
                                <a class="consult LOGCLICK" data-bl="agentim" data-el="1000001000071144" title="在线咨询" data-role="lianjiaim-createtalk" data-ucid="1000001000071144" data-source-port="PC:xinfang_lianjia_project_shouping" data-source-extends="{&quot;house_code&quot;:&quot;bgyfhgjggafscm&quot;}" data-xftrack="10256"></a></div>
                    <div class="resblock-tag">
                                                    <span>小户型</span>
                                                    <span>绿化率高</span>
                        
                    </div>
                    <div class="resblock-price">
                        <div class="main-price">
                                                            <span class="number"> 30600</span>
                                <span class="desc">&nbsp;元 / 平 (均价)</span>
                                                    </div>
                                                                                <div class="second">总价 280 万 / 套起</div>
                                                                        </div>
                                            <div class="resblock-follow" data-follow="noFollow">关注</div>
                                    </div>
            </li>
                        <li class="resblock-list post_ulog_exposure_scroll has-results" data-project-name="ylggafscs" data-ulog-exposure="xinfangpc_show=20005&amp;location=2&amp;project_name=ylggafscs&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268417&quot;,&quot;fb_item_location&quot;:&quot;1&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100118&quot;}" has_been_exposed="1">
                <a href="/loupan/p_ylggafscs/" class="resblock-img-wrapper " title="银领公馆" data-xftrack="10138" data-other-action="location=2&amp;project_name=ylggafscs&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268417&quot;,&quot;fb_item_location&quot;:&quot;1&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100118&quot;}" target="_blank" data-source-type="recommend_projectlist" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268417&quot;,&quot;fb_item_location&quot;:&quot;1&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100118&quot;}">
                    <img alt="银领公馆楼盘图片" class="lj-lazy" data-original="https://image1.ljcdn.com/hdic-resblock/1b1f5bbf-0e98-4190-9e8a-0ad79d33eee2.jpg.592x432.jpg" src="https://image1.ljcdn.com/hdic-resblock/1b1f5bbf-0e98-4190-9e8a-0ad79d33eee2.jpg.592x432.jpg" style="display: inline;">
                    <ul class="icon-wrapper">
                        
                        
                            
                            
                        
                        
                        
                            
                                
                                
                            
                        
                        
                            
                                
                                
                            
                        
                                            </ul>
                    
                    <div class="watermark">效果图</div>
                </a>
                <div class="resblock-desc-wrapper">
                    <div class="resblock-name">
                        <a href="/loupan/p_ylggafscs/" class="name " target="_blank" data-xftrack="10138" data-other-action="location=2&amp;project_name=ylggafscs&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268417&quot;,&quot;fb_item_location&quot;:&quot;1&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100118&quot;}" data-source-type="recommend_projectlist" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268417&quot;,&quot;fb_item_location&quot;:&quot;1&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100118&quot;}">银领公馆</a>
                        <span class="resblock-type" style="background: #FB9252;">住宅</span>
                        <span class="sale-status" style="background: #53CC9A;">在售</span>
                    </div>
                    <div class="resblock-location">
                        <span>龙岗区</span>
                        <i class="split"> /</i>
                        <span> 布吉大芬</span>
                        <i class="split"> / </i>
                        <a href="/loupan/p_ylggafscs/#around" target="_blank" data-xftrack="10254" data-other-action="strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268417&quot;,&quot;fb_item_location&quot;:&quot;1&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100118&quot;}">龙岗布澜路与龙岗大道交汇处</a>
                    </div>
                    <a class="resblock-room" href="/loupan/p_ylggafscs/#house-online" data-xftrack="10255" target="_blank" data-other-action="strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268417&quot;,&quot;fb_item_location&quot;:&quot;1&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100118&quot;}" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268417&quot;,&quot;fb_item_location&quot;:&quot;1&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100118&quot;}">
                                                    <span> 2 室</span>
                                                            <i class="split"> /</i>
                                                                                <span>3 室</span>
                                                    
                    </a>
                    <div class="resblock-area">
                        <span>建面 47-79㎡</span>
                    </div>
                    <div class="resblock-agent"><span class="agent">新房顾问：周庭锐</span>
                                <a class="consult LOGCLICK" data-bl="agentim" data-el="1000000023106155" title="在线咨询" data-role="lianjiaim-createtalk" data-ucid="1000000023106155" data-source-port="PC:xinfang_lianjia_project_shouping" data-source-extends="{&quot;house_code&quot;:&quot;ylggafscs&quot;}" data-xftrack="10256"></a></div>
                    <div class="resblock-tag">
                                                    <span>小户型</span>
                                                    <span>绿化率高</span>
                        
                    </div>
                    <div class="resblock-price">
                        <div class="main-price">
                                                            <span class="number"> 49000</span>
                                <span class="desc">&nbsp;元 / 平 (均价)</span>
                                                    </div>
                                                                                <div class="second">总价 367 万 / 套起</div>
                                                                        </div>
                                            <div class="resblock-follow" data-follow="noFollow">关注</div>
                                    </div>
            </li>
                        <li class="resblock-list post_ulog_exposure_scroll has-results" data-project-name="dglsljafsgl" data-ulog-exposure="xinfangpc_show=20005&amp;location=3&amp;project_name=dglsljafsgl&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268418&quot;,&quot;fb_item_location&quot;:&quot;2&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100215&quot;}" has_been_exposed="1">
                <a href="/loupan/p_dglsljafsgl/" class="resblock-img-wrapper " title="东关乐尚林居" data-xftrack="10138" data-other-action="location=3&amp;project_name=dglsljafsgl&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268418&quot;,&quot;fb_item_location&quot;:&quot;2&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100215&quot;}" target="_blank" data-source-type="recommend_projectlist" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268418&quot;,&quot;fb_item_location&quot;:&quot;2&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100215&quot;}">
                    <img alt="东关乐尚林居楼盘图片" class="lj-lazy" data-original="https://image1.ljcdn.com/hdic-resblock/7d999177-d4e1-4984-a76b-9c193482a769.jpg.592x432.jpg" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif">
                    <ul class="icon-wrapper">
                        
                        
                            
                            
                        
                        
                        
                            
                                
                                
                            
                        
                        
                            
                                
                                
                            
                        
                                            </ul>
                                        <div class="discount">补贴</div>
                    
                    <div class="watermark">效果图</div>
                </a>
                <div class="resblock-desc-wrapper">
                    <div class="resblock-name">
                        <a href="/loupan/p_dglsljafsgl/" class="name " target="_blank" data-xftrack="10138" data-other-action="location=3&amp;project_name=dglsljafsgl&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268418&quot;,&quot;fb_item_location&quot;:&quot;2&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100215&quot;}" data-source-type="recommend_projectlist" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268418&quot;,&quot;fb_item_location&quot;:&quot;2&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100215&quot;}">东关乐尚林居</a>
                        <span class="resblock-type" style="background: #FB9252;">住宅</span>
                        <span class="sale-status" style="background: #53CC9A;">在售</span>
                    </div>
                    <div class="resblock-location">
                        <span>南山区</span>
                        <i class="split"> /</i>
                        <span> 南头</span>
                        <i class="split"> / </i>
                        <a href="/loupan/p_dglsljafsgl/#around" target="_blank" data-xftrack="10254" data-other-action="strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268418&quot;,&quot;fb_item_location&quot;:&quot;2&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100215&quot;}">南山同乐中山园路西侧</a>
                    </div>
                    <a class="resblock-room" href="/loupan/p_dglsljafsgl/#house-online" data-xftrack="10255" target="_blank" data-other-action="strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268418&quot;,&quot;fb_item_location&quot;:&quot;2&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100215&quot;}" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268418&quot;,&quot;fb_item_location&quot;:&quot;2&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100215&quot;}">
                                                    <span> 5 室</span>
                                                    
                    </a>
                    <div class="resblock-area">
                        <span>建面 80-177㎡</span>
                    </div>
                    <div class="resblock-agent"><span class="agent">新房顾问：安鸿</span>
                                <a class="consult LOGCLICK" data-bl="agentim" data-el="1000000010081502" title="在线咨询" data-role="lianjiaim-createtalk" data-ucid="1000000010081502" data-source-port="PC:xinfang_lianjia_project_shouping" data-source-extends="{&quot;house_code&quot;:&quot;dglsljafsgl&quot;}" data-xftrack="10256"></a></div>
                    <div class="resblock-tag">
                                                    <span>品牌房企</span>
                                                    <span>小户型</span>
                                                    <span>绿化率高</span>
                        
                    </div>
                    <div class="resblock-price">
                        <div class="main-price">
                                                            <span class="number"> 76000</span>
                                <span class="desc">&nbsp;元 / 平 (均价)</span>
                                                    </div>
                                                                                <div class="second">总价 1350 万 / 套起</div>
                                                                        </div>
                                            <div class="resblock-follow" data-follow="noFollow">关注</div>
                                    </div>
            </li>
                        <li class="resblock-list post_ulog_exposure_scroll has-results" data-project-name="fhfhtyafslk" data-ulog-exposure="xinfangpc_show=20005&amp;location=4&amp;project_name=fhfhtyafslk&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268419&quot;,&quot;fb_item_location&quot;:&quot;3&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100344&quot;}">
                <a href="/loupan/p_fhfhtyafslk/" class="resblock-img-wrapper " title="富宏凤凰天誉" data-xftrack="10138" data-other-action="location=4&amp;project_name=fhfhtyafslk&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268419&quot;,&quot;fb_item_location&quot;:&quot;3&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100344&quot;}" target="_blank" data-source-type="recommend_projectlist" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268419&quot;,&quot;fb_item_location&quot;:&quot;3&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100344&quot;}">
                    <img alt="富宏凤凰天誉楼盘图片" class="lj-lazy" data-original="https://image1.ljcdn.com/hdic-resblock/a35e4fcd-edfe-43da-9f4c-e16cae1231dd.jpg.592x432.jpg" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif">
                    <ul class="icon-wrapper">
                        
                        
                            
                            
                        
                        
                        
                            
                                
                                
                            
                        
                        
                            
                                
                                
                            
                        
                                            </ul>
                    
                    <div class="watermark">效果图</div>
                </a>
                <div class="resblock-desc-wrapper">
                    <div class="resblock-name">
                        <a href="/loupan/p_fhfhtyafslk/" class="name " target="_blank" data-xftrack="10138" data-other-action="location=4&amp;project_name=fhfhtyafslk&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268419&quot;,&quot;fb_item_location&quot;:&quot;3&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100344&quot;}" data-source-type="recommend_projectlist" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268419&quot;,&quot;fb_item_location&quot;:&quot;3&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100344&quot;}">富宏凤凰天誉</a>
                        <span class="resblock-type" style="background: #FB9252;">住宅</span>
                        <span class="sale-status" style="background: #53CC9A;">在售</span>
                    </div>
                    <div class="resblock-location">
                        <span>宝安区</span>
                        <i class="split"> /</i>
                        <span> 西乡</span>
                        <i class="split"> / </i>
                        <a href="/loupan/p_fhfhtyafslk/#around" target="_blank" data-xftrack="10254" data-other-action="strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268419&quot;,&quot;fb_item_location&quot;:&quot;3&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100344&quot;}">西乡前进二路与宝田一路交汇处</a>
                    </div>
                    <a class="resblock-room" href="/loupan/p_fhfhtyafslk/#house-online" data-xftrack="10255" target="_blank" data-other-action="strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268419&quot;,&quot;fb_item_location&quot;:&quot;3&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100344&quot;}" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268419&quot;,&quot;fb_item_location&quot;:&quot;3&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100344&quot;}">
                                                    <span> 2 室</span>
                                                            <i class="split"> /</i>
                                                                                <span>3 室</span>
                                                    
                    </a>
                    <div class="resblock-area">
                        <span>建面 80-117㎡</span>
                    </div>
                    <div class="resblock-agent"><span class="agent">新房顾问：李路</span>
                                <a class="consult LOGCLICK" data-bl="agentim" data-el="1000000020345066" title="在线咨询" data-role="lianjiaim-createtalk" data-ucid="1000000020345066" data-source-port="PC:xinfang_lianjia_project_shouping" data-source-extends="{&quot;house_code&quot;:&quot;fhfhtyafslk&quot;}" data-xftrack="10256"></a></div>
                    <div class="resblock-tag">
                                                    <span>绿化率高</span>
                                                    <span>车位充足</span>
                        
                    </div>
                    <div class="resblock-price">
                        <div class="main-price">
                                                            <span class="number"> 65000</span>
                                <span class="desc">&nbsp;元 / 平 (均价)</span>
                                                    </div>
                                                                                <div class="second">总价 510 万 / 套起</div>
                                                                        </div>
                                            <div class="resblock-follow" data-follow="noFollow">关注</div>
                                    </div>
            </li>
                        <li class="resblock-list post_ulog_exposure_scroll has-results" data-project-name="qhjrzxafsvv" data-ulog-exposure="xinfangpc_show=20005&amp;location=5&amp;project_name=qhjrzxafsvv&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268420&quot;,&quot;fb_item_location&quot;:&quot;4&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100615&quot;}">
                <a href="/loupan/p_qhjrzxafsvv/" class="resblock-img-wrapper " title="前海金融中心" data-xftrack="10138" data-other-action="location=5&amp;project_name=qhjrzxafsvv&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268420&quot;,&quot;fb_item_location&quot;:&quot;4&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100615&quot;}" target="_blank" data-source-type="recommend_projectlist" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268420&quot;,&quot;fb_item_location&quot;:&quot;4&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100615&quot;}">
                    <img alt="前海金融中心楼盘图片" class="lj-lazy" data-original="https://image1.ljcdn.com/newhouse-user-image/4bfe71aaae5305b84431a8dff000f299.jpg.592x432.jpg" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif">
                    <ul class="icon-wrapper">
                        
                        
                            
                            
                        
                        
                        
                            
                                
                                
                            
                        
                        
                            
                                
                                
                            
                        
                                            </ul>
                    
                    <div class="watermark">效果图</div>
                </a>
                <div class="resblock-desc-wrapper">
                    <div class="resblock-name">
                        <a href="/loupan/p_qhjrzxafsvv/" class="name " target="_blank" data-xftrack="10138" data-other-action="location=5&amp;project_name=qhjrzxafsvv&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268420&quot;,&quot;fb_item_location&quot;:&quot;4&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100615&quot;}" data-source-type="recommend_projectlist" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268420&quot;,&quot;fb_item_location&quot;:&quot;4&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100615&quot;}">前海金融中心</a>
                        <span class="resblock-type" style="background: #59A5EB;">写字楼</span>
                        <span class="sale-status" style="background: #53CC9A;">在售</span>
                    </div>
                    <div class="resblock-location">
                        <span>南山区</span>
                        <i class="split"> /</i>
                        <span> 前海</span>
                        <i class="split"> / </i>
                        <a href="/loupan/p_qhjrzxafsvv/#around" target="_blank" data-xftrack="10254" data-other-action="strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268420&quot;,&quot;fb_item_location&quot;:&quot;4&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100615&quot;}">深圳前海临海大道与桂湾三路交汇处</a>
                    </div>
                    <a class="resblock-room" href="/loupan/p_qhjrzxafsvv/#house-online" data-xftrack="10255" target="_blank" data-other-action="strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268420&quot;,&quot;fb_item_location&quot;:&quot;4&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100615&quot;}" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268420&quot;,&quot;fb_item_location&quot;:&quot;4&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100615&quot;}">
                        
                    </a>
                    <div class="resblock-area">
                        <span></span>
                    </div>
                    <div class="resblock-agent"><span class="agent">新房顾问：刘春亮</span>
                                <a class="consult LOGCLICK" data-bl="agentim" data-el="1000000010099774" title="在线咨询" data-role="lianjiaim-createtalk" data-ucid="1000000010099774" data-source-port="PC:xinfang_lianjia_project_shouping" data-source-extends="{&quot;house_code&quot;:&quot;qhjrzxafsvv&quot;}" data-xftrack="10256"></a></div>
                    <div class="resblock-tag">
                                                    <span>绿化率高</span>
                                                    <span>低密度</span>
                                                    <span>车位充足</span>
                        
                    </div>
                    <div class="resblock-price">
                        <div class="main-price">
                                                            <span class="number"> 95000</span>
                                <span class="desc">&nbsp;元 / 平 (均价)</span>
                                                    </div>
                                                                                                </div>
                                            <div class="resblock-follow" data-follow="noFollow">关注</div>
                                    </div>
            </li>
                        <li class="resblock-list post_ulog_exposure_scroll has-results" data-project-name="hsafswo" data-ulog-exposure="xinfangpc_show=20005&amp;location=6&amp;project_name=hsafswo&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268421&quot;,&quot;fb_item_location&quot;:&quot;5&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100634&quot;}">
                <a href="/loupan/p_hsafswo/" class="resblock-img-wrapper " title="红山6979" data-xftrack="10138" data-other-action="location=6&amp;project_name=hsafswo&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268421&quot;,&quot;fb_item_location&quot;:&quot;5&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100634&quot;}" target="_blank" data-source-type="recommend_projectlist" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268421&quot;,&quot;fb_item_location&quot;:&quot;5&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100634&quot;}">
                    <img alt="红山6979楼盘图片" class="lj-lazy" data-original="https://image1.ljcdn.com/hdic-resblock/3c377db6-5e19-45ca-873d-36a9b0ec7ed4.jpg.592x432.jpg" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif">
                    <ul class="icon-wrapper">
                        
                        
                            
                            
                        
                        
                        
                            
                                
                                
                            
                        
                        
                            
                                
                                
                            
                        
                                            </ul>
                                        <div class="discount">全款 9.8 折  贷款 9.9 折</div>
                    
                    <div class="watermark">效果图</div>
                </a>
                <div class="resblock-desc-wrapper">
                    <div class="resblock-name">
                        <a href="/loupan/p_hsafswo/" class="name " target="_blank" data-xftrack="10138" data-other-action="location=6&amp;project_name=hsafswo&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268421&quot;,&quot;fb_item_location&quot;:&quot;5&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100634&quot;}" data-source-type="recommend_projectlist" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268421&quot;,&quot;fb_item_location&quot;:&quot;5&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100634&quot;}">红山 6979</a>
                        <span class="resblock-type" style="background: #DAAC24;"> 底商</span>
                        <span class="sale-status" style="background: #53CC9A;">在售</span>
                    </div>
                    <div class="resblock-location">
                        <span>龙华区</span>
                        <i class="split"> /</i>
                        <span> 红山</span>
                        <i class="split"> / </i>
                        <a href="/loupan/p_hsafswo/#around" target="_blank" data-xftrack="10254" data-other-action="strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268421&quot;,&quot;fb_item_location&quot;:&quot;5&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100634&quot;}">腾龙路与中梅路交汇处东侧</a>
                    </div>
                    <a class="resblock-room" href="/loupan/p_hsafswo/#house-online" data-xftrack="10255" target="_blank" data-other-action="strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268421&quot;,&quot;fb_item_location&quot;:&quot;5&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100634&quot;}" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268421&quot;,&quot;fb_item_location&quot;:&quot;5&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100634&quot;}">
                        
                    </a>
                    <div class="resblock-area">
                        <span></span>
                    </div>
                    <div class="resblock-agent"><span class="agent">新房顾问：余金梁</span>
                                <a class="consult LOGCLICK" data-bl="agentim" data-el="1000000020125955" title="在线咨询" data-role="lianjiaim-createtalk" data-ucid="1000000020125955" data-source-port="PC:xinfang_lianjia_project_shouping" data-source-extends="{&quot;house_code&quot;:&quot;hsafswo&quot;}" data-xftrack="10256"></a></div>
                    <div class="resblock-tag">
                                                    <span>品牌房企</span>
                                                    <span>现房</span>
                                                    <span>绿化率高</span>
                                                    <span>车位充足</span>
                                                    <span>低密度</span>
                        
                    </div>
                    <div class="resblock-price">
                        <div class="main-price">
                                                            <span class="number"> 140000</span>
                                <span class="desc">&nbsp;元 / 平 (均价)</span>
                                                    </div>
                                                                                                </div>
                                            <div class="resblock-follow" data-follow="noFollow">关注</div>
                                    </div>
            </li>
                        <li class="resblock-list post_ulog_exposure_scroll has-results" data-project-name="tjggafsxo" data-ulog-exposure="xinfangpc_show=20005&amp;location=7&amp;project_name=tjggafsxo&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268422&quot;,&quot;fb_item_location&quot;:&quot;6&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100660&quot;}">
                <a href="/loupan/p_tjggafsxo/" class="resblock-img-wrapper " title="天玑公馆" data-xftrack="10138" data-other-action="location=7&amp;project_name=tjggafsxo&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268422&quot;,&quot;fb_item_location&quot;:&quot;6&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100660&quot;}" target="_blank" data-source-type="recommend_projectlist" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268422&quot;,&quot;fb_item_location&quot;:&quot;6&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100660&quot;}">
                    <img alt="天玑公馆楼盘图片" class="lj-lazy" data-original="https://image1.ljcdn.com/newhouse-user-image/phpYmT19X1543392878.png.592x432.jpg" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif">
                    <ul class="icon-wrapper">
                        
                        
                            
                            
                        
                        
                        
                            
                                
                                
                            
                        
                        
                            
                                
                                
                            
                        
                                            </ul>
                    
                    <div class="watermark">效果图</div>
                </a>
                <div class="resblock-desc-wrapper">
                    <div class="resblock-name">
                        <a href="/loupan/p_tjggafsxo/" class="name " target="_blank" data-xftrack="10138" data-other-action="location=7&amp;project_name=tjggafsxo&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268422&quot;,&quot;fb_item_location&quot;:&quot;6&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100660&quot;}" data-source-type="recommend_projectlist" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268422&quot;,&quot;fb_item_location&quot;:&quot;6&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100660&quot;}">天玑公馆</a>
                        <span class="resblock-type" style="background: #4CC1EC;">商业类</span>
                        <span class="sale-status" style="background: #53CC9A;">在售</span>
                    </div>
                    <div class="resblock-location">
                        <span>龙华区</span>
                        <i class="split"> /</i>
                        <span> 龙华中心</span>
                        <i class="split"> / </i>
                        <a href="/loupan/p_tjggafsxo/#around" target="_blank" data-xftrack="10254" data-other-action="strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268422&quot;,&quot;fb_item_location&quot;:&quot;6&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100660&quot;}">港铁四号线清湖北站（建设中）旁</a>
                    </div>
                    <a class="resblock-room" href="/loupan/p_tjggafsxo/#house-online" data-xftrack="10255" target="_blank" data-other-action="strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268422&quot;,&quot;fb_item_location&quot;:&quot;6&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100660&quot;}" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268422&quot;,&quot;fb_item_location&quot;:&quot;6&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100660&quot;}">
                                                    <span> 1 室</span>
                                                    
                    </a>
                    <div class="resblock-area">
                        <span>建面 36-40㎡</span>
                    </div>
                    <div class="resblock-agent"><span class="agent">新房顾问：肖枫</span>
                                <a class="consult LOGCLICK" data-bl="agentim" data-el="1000000020175700" title="在线咨询" data-role="lianjiaim-createtalk" data-ucid="1000000020175700" data-source-port="PC:xinfang_lianjia_project_shouping" data-source-extends="{&quot;house_code&quot;:&quot;tjggafsxo&quot;}" data-xftrack="10256"></a></div>
                    <div class="resblock-tag">
                                                    <span>品牌房企</span>
                                                    <span>小户型</span>
                                                    <span>绿化率高</span>
                        
                    </div>
                    <div class="resblock-price">
                        <div class="main-price">
                                                            <span class="number"> 45000</span>
                                <span class="desc">&nbsp;元 / 平 (均价)</span>
                                                    </div>
                                                                                <div class="second">总价 155 万 / 套起</div>
                                                                        </div>
                                            <div class="resblock-follow" data-follow="noFollow">关注</div>
                                    </div>
            </li>
                        <li class="resblock-list post_ulog_exposure_scroll has-results" data-project-name="zltygcaftbd" data-ulog-exposure="xinfangpc_show=20005&amp;location=8&amp;project_name=zltygcaftbd&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268423&quot;,&quot;fb_item_location&quot;:&quot;7&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100753&quot;}">
                <a href="/loupan/p_zltygcaftbd/" class="resblock-img-wrapper " title="中粮天悦广场" data-xftrack="10138" data-other-action="location=8&amp;project_name=zltygcaftbd&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268423&quot;,&quot;fb_item_location&quot;:&quot;7&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100753&quot;}" target="_blank" data-source-type="recommend_projectlist" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268423&quot;,&quot;fb_item_location&quot;:&quot;7&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100753&quot;}">
                    <img alt="中粮天悦广场楼盘图片" class="lj-lazy" data-original="https://image1.ljcdn.com/hdic-resblock/3080f200-c699-4a89-b7e9-0abc583782c5.png.592x432.jpg" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif">
                    <ul class="icon-wrapper">
                        
                        
                            
                            
                        
                        
                        
                            
                                
                                
                            
                        
                        
                            
                                
                                
                            
                        
                                            </ul>
                    
                    <div class="watermark">效果图</div>
                </a>
                <div class="resblock-desc-wrapper">
                    <div class="resblock-name">
                        <a href="/loupan/p_zltygcaftbd/" class="name " target="_blank" data-xftrack="10138" data-other-action="location=8&amp;project_name=zltygcaftbd&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268423&quot;,&quot;fb_item_location&quot;:&quot;7&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100753&quot;}" data-source-type="recommend_projectlist" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268423&quot;,&quot;fb_item_location&quot;:&quot;7&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100753&quot;}">中粮天悦广场</a>
                        <span class="resblock-type" style="background: #DAAC24;">底商</span>
                        <span class="sale-status" style="background: #53CC9A;">在售</span>
                    </div>
                    <div class="resblock-location">
                        <span>宝安区</span>
                        <i class="split"> /</i>
                        <span> 新安</span>
                        <i class="split"> / </i>
                        <a href="/loupan/p_zltygcaftbd/#around" target="_blank" data-xftrack="10254" data-other-action="strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268423&quot;,&quot;fb_item_location&quot;:&quot;7&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100753&quot;}">深圳宝安新安二路与公园路交汇处</a>
                    </div>
                    <a class="resblock-room" href="/loupan/p_zltygcaftbd/#house-online" data-xftrack="10255" target="_blank" data-other-action="strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268423&quot;,&quot;fb_item_location&quot;:&quot;7&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100753&quot;}" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268423&quot;,&quot;fb_item_location&quot;:&quot;7&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100753&quot;}">
                        
                    </a>
                    <div class="resblock-area">
                        <span></span>
                    </div>
                    <div class="resblock-agent"><span class="agent">新房顾问：吴光第</span>
                                <a class="consult LOGCLICK" data-bl="agentim" data-el="1000000023008538" title="在线咨询" data-role="lianjiaim-createtalk" data-ucid="1000000023008538" data-source-port="PC:xinfang_lianjia_project_shouping" data-source-extends="{&quot;house_code&quot;:&quot;zltygcaftbd&quot;}" data-xftrack="10256"></a></div>
                    <div class="resblock-tag">
                                                    <span>绿化率高</span>
                        
                    </div>
                    <div class="resblock-price">
                        <div class="main-price">
                                                            <span class="number"> 150000</span>
                                <span class="desc">&nbsp;元 / 平 (均价)</span>
                                                    </div>
                                                                                                </div>
                                            <div class="resblock-follow" data-follow="noFollow">关注</div>
                                    </div>
            </li>
                        <li class="resblock-list post_ulog_exposure_scroll has-results" data-project-name="yrdljaftjd" data-ulog-exposure="xinfangpc_show=20005&amp;location=9&amp;project_name=yrdljaftjd&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268424&quot;,&quot;fb_item_location&quot;:&quot;8&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100961&quot;}">
                <a href="/loupan/p_yrdljaftjd/" class="resblock-img-wrapper " title="怡瑞达乐郡" data-xftrack="10138" data-other-action="location=9&amp;project_name=yrdljaftjd&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268424&quot;,&quot;fb_item_location&quot;:&quot;8&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100961&quot;}" target="_blank" data-source-type="recommend_projectlist" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268424&quot;,&quot;fb_item_location&quot;:&quot;8&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100961&quot;}">
                    <img alt="怡瑞达乐郡楼盘图片" class="lj-lazy" data-original="https://image1.ljcdn.com/hdic-resblock/6692dcd5-927f-4368-a92e-7aec9a13cab2.jpg.592x432.jpg" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif">
                    <ul class="icon-wrapper">
                        
                        
                            
                            
                        
                        
                        
                            
                                
                                
                            
                        
                        
                            
                                
                                
                            
                        
                                            </ul>
                    
                    <div class="watermark">效果图</div>
                </a>
                <div class="resblock-desc-wrapper">
                    <div class="resblock-name">
                        <a href="/loupan/p_yrdljaftjd/" class="name " target="_blank" data-xftrack="10138" data-other-action="location=9&amp;project_name=yrdljaftjd&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268424&quot;,&quot;fb_item_location&quot;:&quot;8&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100961&quot;}" data-source-type="recommend_projectlist" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268424&quot;,&quot;fb_item_location&quot;:&quot;8&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100961&quot;}">怡瑞达乐郡</a>
                        <span class="resblock-type" style="background: #FB9252;">住宅</span>
                        <span class="sale-status" style="background: #53CC9A;">在售</span>
                    </div>
                    <div class="resblock-location">
                        <span>龙岗区</span>
                        <i class="split"> /</i>
                        <span> 龙岗宝荷</span>
                        <i class="split"> / </i>
                        <a href="/loupan/p_yrdljaftjd/#around" target="_blank" data-xftrack="10254" data-other-action="strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268424&quot;,&quot;fb_item_location&quot;:&quot;8&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100961&quot;}">龙岗街道深汕路与乐园路交汇处南侧</a>
                    </div>
                    <a class="resblock-room" href="/loupan/p_yrdljaftjd/#house-online" data-xftrack="10255" target="_blank" data-other-action="strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268424&quot;,&quot;fb_item_location&quot;:&quot;8&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100961&quot;}" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268424&quot;,&quot;fb_item_location&quot;:&quot;8&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;100961&quot;}">
                                                    <span> 3 室</span>
                                                    
                    </a>
                    <div class="resblock-area">
                        <span>建面 85-89㎡</span>
                    </div>
                    <div class="resblock-agent"><span class="agent">新房顾问：张振磊</span>
                                <a class="consult LOGCLICK" data-bl="agentim" data-el="1000000020390637" title="在线咨询" data-role="lianjiaim-createtalk" data-ucid="1000000020390637" data-source-port="PC:xinfang_lianjia_project_shouping" data-source-extends="{&quot;house_code&quot;:&quot;yrdljaftjd&quot;}" data-xftrack="10256"></a></div>
                    <div class="resblock-tag">
                                                    <span>绿化率高</span>
                                                    <span>低密度</span>
                        
                    </div>
                    <div class="resblock-price">
                        <div class="main-price">
                                                            <span class="number"> 34000</span>
                                <span class="desc">&nbsp;元 / 平 (均价)</span>
                                                    </div>
                                                                                <div class="second">总价 290 万 / 套起</div>
                                                                        </div>
                                            <div class="resblock-follow" data-follow="noFollow">关注</div>
                                    </div>
            </li>
                        <li class="resblock-list post_ulog_exposure_scroll has-results" data-project-name="mjhyxggaavmw" data-ulog-exposure="xinfangpc_show=20005&amp;location=10&amp;project_name=mjhyxggaavmw&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268425&quot;,&quot;fb_item_location&quot;:&quot;9&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;14530&quot;}">
                <a href="/loupan/p_mjhyxggaavmw/" class="resblock-img-wrapper " title="满京华云晓公馆" data-xftrack="10138" data-other-action="location=10&amp;project_name=mjhyxggaavmw&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268425&quot;,&quot;fb_item_location&quot;:&quot;9&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;14530&quot;}" target="_blank" data-source-type="recommend_projectlist" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268425&quot;,&quot;fb_item_location&quot;:&quot;9&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;14530&quot;}">
                    <img alt="满京华云晓公馆楼盘图片" class="lj-lazy" data-original="https://image1.ljcdn.com/hdic-resblock/7fedf9f6-8987-4dbd-ae87-66167c3d837d.jpg.592x432.jpg" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif">
                    <ul class="icon-wrapper">
                        
                        
                            
                            
                        
                        
                        
                            
                                
                                
                            
                        
                        
                            
                                
                                
                            
                        
                                            </ul>
                    
                    <div class="watermark">效果图</div>
                </a>
                <div class="resblock-desc-wrapper">
                    <div class="resblock-name">
                        <a href="/loupan/p_mjhyxggaavmw/" class="name " target="_blank" data-xftrack="10138" data-other-action="location=10&amp;project_name=mjhyxggaavmw&amp;recommend_log_info=&amp;strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268425&quot;,&quot;fb_item_location&quot;:&quot;9&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;14530&quot;}" data-source-type="recommend_projectlist" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268425&quot;,&quot;fb_item_location&quot;:&quot;9&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;14530&quot;}">满京华云晓公馆</a>
                        <span class="resblock-type" style="background: #FB9252;">住宅</span>
                        <span class="sale-status" style="background: #53CC9A;">在售</span>
                    </div>
                    <div class="resblock-location">
                        <span>宝安区</span>
                        <i class="split"> /</i>
                        <span> 西乡</span>
                        <i class="split"> / </i>
                        <a href="/loupan/p_mjhyxggaavmw/#around" target="_blank" data-xftrack="10254" data-other-action="strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268425&quot;,&quot;fb_item_location&quot;:&quot;9&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;14530&quot;}">西乡黄田村 107 国道俊景园北侧</a>
                    </div>
                    <a class="resblock-room" href="/loupan/p_mjhyxggaavmw/#house-online" data-xftrack="10255" target="_blank" data-other-action="strategy_info={&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268425&quot;,&quot;fb_item_location&quot;:&quot;9&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;14530&quot;}" data-strategy-info="{&quot;fb_query_id&quot;:&quot;174611193949388800&quot;,&quot;fb_expo_id&quot;:&quot;174611193966268425&quot;,&quot;fb_item_location&quot;:&quot;9&quot;,&quot;fb_service_id&quot;:&quot;1012810002&quot;,&quot;fb_ab_test_flag&quot;:&quot;[]&quot;,&quot;fb_item_id&quot;:&quot;14530&quot;}">
                                                    <span> 2 室</span>
                                                            <i class="split"> /</i>
                                                                                <span>3 室</span>
                                                            <i class="split"> /</i>
                                                                                <span>4 室</span>
                                                    
                    </a>
                    <div class="resblock-area">
                        <span>建面 62-155㎡</span>
                    </div>
                    <div class="resblock-agent"><span class="agent">新房顾问：郭灵杰</span>
                                <a class="consult LOGCLICK" data-bl="agentim" data-el="1000000026032075" title="在线咨询" data-role="lianjiaim-createtalk" data-ucid="1000000026032075" data-source-port="PC:xinfang_lianjia_project_shouping" data-source-extends="{&quot;house_code&quot;:&quot;mjhyxggaavmw&quot;}" data-xftrack="10256"></a></div>
                    <div class="resblock-tag">
                                                    <span>小户型</span>
                                                    <span>现房</span>
                                                    <span>绿化率高</span>
                                                    <span>复式</span>
                        
                    </div>
                    <div class="resblock-price">
                        <div class="main-price">
                                                            <span class="number"> 55000</span>
                                <span class="desc">&nbsp;元 / 平 (均价)</span>
                                                    </div>
                                                                                <div class="second">总价 460 万 / 套起</div>
                                                                        </div>
                                            <div class="resblock-follow" data-follow="noFollow">关注</div>
                                    </div>
            </li>
            
            
        </ul>"""
NOT_EXIST = -1
soup = BeautifulSoup(html, 'lxml')
ul = soup.find_all(attrs={'class': 'resblock-list post_ulog_exposure_scroll has-results'})
for li in ul:
    loupan = li.find_all(attrs={'class': 'name'})[0].text
    loupan_url = li.find_all(attrs={'class': 'name'})[0].attrs['href']
    wuyetype = li.find_all(attrs={'class': 'resblock-type'})[0].text
    sale_status = li.find_all(attrs={'class': 'sale-status'})[0].text
    img_url = li.find_all(attrs={'class': 'lj-lazy'})[0].attrs['data-original']
    location = li.find_all(attrs={'class': 'resblock-location'})[0].text.replace('\n', '').split('/')
    huxing = li.find_all(attrs={'class': 'resblock-room'})[0].text.replace('\n', '')
    tmp_area = li.find_all(attrs={'class': 'resblock-area'})[0].text.replace(' ', '').replace('\n', '').replace('建面',
                                                                                                                '').replace('㎡', '')
    if tmp_area == '':
        area = []
    else:
        list = tmp_area.split('-')
        area = [int(i) for i in list]
    main_price = li.find_all(attrs={'class': 'number'})
    if (main_price != []):
        main_price = int(main_price[0].text.replace(' ',''))
    else:
        main_price = NOT_EXIST
    main_price_desc = li.find_all(attrs={'class': 'desc'})
    if main_price_desc != []:
        main_price_desc = main_price_desc[0].text
    else:
        main_price_desc = NOT_EXIST
    second_price = li.find_all(attrs={'class': 'second'})
    if (second_price != []):
        second_price = second_price[0].text.replace('总价', '').replace(' 万 / 套起', '').replace(' ', '')
    else:
        second_price = NOT_EXIST
    tag = li.find_all(attrs={'class':'resblock-tag'})[0].text.replace('','').split('\n')
    tag = tag[1:-1]
    print(loupan)
    print(loupan_url)
    print(wuyetype)
    print(sale_status)
    print(img_url)
    print(location)
    print(huxing)
    print(area)
    print(main_price)
    print(main_price_desc)
    print(second_price)
    print(tag)
    exit()
