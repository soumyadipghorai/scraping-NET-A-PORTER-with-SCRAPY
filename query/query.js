// Q4. 
[
  {
    $unwind : {
      path: '$brand',
      preserveNullAndEmptyArrays: true
    }
  },
  {
    $group: {
      _id: null,
      distinctBrands: {$addToSet: '$brand'}
    }
  }
]

