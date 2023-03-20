# Mapping trace
병원에서 쓰는 처방, 진당 등의 코드들이 있는데 주로 병원에서는 로컬의 코드를 사용하지만 여러 기관과 협동 연구를 할 때 코드 표준화 해서 연구를 진행하는데 모든 병원 코드들이 1:1로 표준 코드랑 대응이 되지 않아서 시간에 따라 더 적합한 코드 혹은 신규 코드로 변경이 되었을 때 기록을 남기고 또한 웹 상에서 간편하게 수정을 위해 만들어짐, 여기서 맵핑된 코드들은 나중에 ETL 과정에서 사용 <br><br>

클라우드 서버가 아닌 물리 서버에서 Nginx + gUnicorn 이용해서 배포<br>
front 랑 back 을 django 로 개발 진행<br><br>

## View
summary_cnt : 전체, 도메인 별 맵핑된 수 반환
search_outcome : 검색 결과 반환 함수
summary : index page 로 이동
map_by_excel : 업로드한 엑셀로 맵핑 진행
SearchListView : 검색 결과 반환
EditTableListView : 다중 맵핑 수정 초기 데이터 제공
edit_table_save : 다중 맵핑 수정 결과 저장
edit_save : 단일 맵핑 수정 결과 저장

자세한 사항은 ppt 참고
[smartpv vocab trace webpage.pptx](https://github.com/lakeparkXPA/mapping_trace/files/11019213/smartpv.vocab.trace.webpage.pptx)
