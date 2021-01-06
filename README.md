# download_article
In lab, sometimes I need to download articles and collate relevant information
  
`Demo`:
<table>
  <tr>
    <th>论文信息</th>
    <th>作者</th>
    <th>单位</th>
    <th>国家地区</th>
    <th>头衔</th>
    <th>英文评价</th>
  </tr>
  <tr>
    <td rowspan='3'>Global exponential……, Neural Networks, 19(5),2006标题，期刊，vol(no),pp,year</td>
    <td>aothor-1</td>
    <td>institutions-1</td>
    <td>nation-1</td>
    <td>title-1</td>
    <td  rowspan='3'>English evaluation</td>
  </tr>
  <tr>
    <td>aothor-2</td>
    <td>institutions-2</td>
    <td>nation-1</td>
    <td>title-1</td>
  </tr>
  <tr>
    <td>aothor-2</td>
    <td>institutions-3</td>
    <td>nation-1</td>
    <td>title-1</td>
  </tr>
</table>

根据 Google scholar 导出的CSV文件，进行提取信息：文章引用Citation、作者Author。

- Citation：
  论文的引用信息，格式为：标题，期刊，vol(no),pp,year
  
  目前存在的问题，如果某个数字不存在，会变成NaN，后续有待改进……
  
- Author：
  论文的作者信息
  
  简单的根据 `;` 分开作者姓名
  
其余功能及改进，有待后续进行……
