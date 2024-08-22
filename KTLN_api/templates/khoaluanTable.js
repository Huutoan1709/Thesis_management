import React from 'react';

const KhoaLuanTable = () => {
  return (
    <h1>Hello guys</h1>
  );
};

export default KhoaLuanTable;
//import React, { useState, useEffect } from 'react';
//import axios from 'axios';
//
//function KhoaLuanTable() {
//  const [data, setData] = useState({ results: [], next: null, previous: null });
//
//  useEffect(() => {
//    async function fetchData() {
//      const response = await axios.get('http://127.0.0.1:8000/dskhoaluan/');
//      setData(response.data);
//    }
//    fetchData();
//  }, []);
//
//  return (
//    <div className="container my-5">
//      <h1>Danh sách Khóa Luận</h1>
//      <table className="table table-striped">
//        <thead>
//          <tr>
//            <th>ID</th>
//            <th>Tên</th>
//            <th>Chi tiết</th>
//          </tr>
//        </thead>
//        <tbody>
//          {data.results.map((item) => (
//            <tr key={item.id}>
//              <td>{item.id}</td>
//              <td>{item.ten}</td>
//              <td><a href="#">Xem chi tiết</a></td>
//            </tr>
//          ))}
//        </tbody>
//      </table>
//      <div className="d-flex justify-content-between">
//        {data.previous && (
//          <a href={data.previous} className="btn btn-secondary">
//            Trang trước
//          </a>
//        )}
//        {data.next && (
//          <a href={data.next} className="btn btn-primary">
//            Trang tiếp theo
//          </a>
//        )}
//      </div>
//    </div>
//  );
//}
//
//export default KhoaLuanTable;
