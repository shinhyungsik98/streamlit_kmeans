import streamlit as st
import pandas as pd

def main () :
    st.title('K-means 클러스터링 앱')
    st.text('csv파일을 업로드 하면, 비슷한 유형의 데이터끼리 묶어주는 앱입니다.')

    #1. csv 파일 업로드 
    file = st.file_uploader('csv파일업로드',type=['csv'])

    if file is not None :
        #1-1 판다스의 데이터프레임으로 읽는다.
        df = pd.read_csv(file)

        #1-2 유저한테 데이터프레임 보여준다
        st.dataframe(df)

        #2. nan 데이터 있으면, 삭제한다.
        print(df.isna().sum())

        st.subheader('각 컬럼별 Nan의 갯수입니다')

        st.dataframe(df.isna().sum())

        df.dropna(inplace=True)

        st.info('Nan 이 있으면 해당 데이터는 삭제합니다.')

        #3. 유저한테 컬럼을 선택할수 있도록 하자.
        st.subheader('클러스터링에 사용할 컬럼 선택')
        selected_columns = st.multiselect('X로 사용할 컬럼을 선택하세요', df.columns)

        X= df[selected_columns]


        st.dataframe(X)

        if len(selected_columns ) >=2 :
            pass

            #4. 해당 컬럼의 데이터가 문자열이면, 숫자로 바꿔주자.

            #5. k의 갯수를 1개부터 10개까지 해서 wcss를 구한다.

            #6. elobw method 를 이용해서, 차트로 보여준다.

            #7. 유저가 k의 갯수를 정한다.

            #8. KMeans 수행해서 그룹정보를 가져온다.

            #9. 원래 있던 df에 Grouup 이라는 컬럼을 만들어준다.

            #10. 결과를 파일로 저장한다.

if __name__ == '__main__' :
    main()