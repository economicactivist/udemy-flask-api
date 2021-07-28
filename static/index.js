
alert('connected')
console.log("working?")

// axios.get('/store')
// .then((response) => {console.log(response.data)}, 
// (error) => {console.log(error)})

// const storeData = async () => { 
//   try {
//     const response = await axios.get('/store')
//     console.log(response.data)
//   } catch (error) {
//     console.log(error)
//   }
// }

// storeData()

$.ajax({
    url: '/store',
    type: 'GET',
    success: (data) => {
        console.log(data)
    }
})
