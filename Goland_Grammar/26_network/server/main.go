package main

import (
	"fmt"
	"log"
	"net"
)

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/08/16 16:26
*/

func process(conn net.Conn) {
	defer conn.Close() //关闭conn，一定要关闭

	//循环接收客户端发送的数据
	for {
		//创建一个新的切片
		buf := make([]byte, 1024)

		/*解释 conn.Read(buf)
		  1. 等待客户端通过conn发送信息
		  2. 如果客户端没有wrtie[发送]，那么协程就阻塞在这里
		*/
		fmt.Printf("服务器在等待客户端%s 发送信息。。。\n", conn.RemoteAddr().String())
		n, err := conn.Read(buf) //从conn读取
		if err != nil {
			fmt.Printf("客户端退出 err=%v", err)
			return //!!!别忘记写
		}

		//显示客户端发送的内容到服务器的终端
		fmt.Print(string(buf[:n])) //n是读取到的字节数
	}

}

func main() {

	fmt.Println("服务器开始监听....")
	/* 解释：net.Listen("tcp", "0.0.0.0:8888")
	   (1). tcp 表示使用网络协议是tcp
	   (2). 0.0.0.0:8888 表示在本地监听 8888端口
	*/
	listen, err := net.Listen("tcp", "0.0.0.0:8081")
	if err != nil {
		fmt.Println("listen err=", err)
		return
	}
	//fmt.Printf("listen suc=%v\n", listen)
	defer listen.Close() //延时关闭listen

	//循环等待客户端来链接我
	for {
		log.Println("等待客户端来链接....")
		//等待客户端链接
		conn, err := listen.Accept()
		if err != nil {
			fmt.Println("Accept() err=", err)

		} else {
			fmt.Printf("Accept() success con=%v 客户端ip=%v\n", conn, conn.RemoteAddr().String())
		}
		//这里准备其一个协程，为客户端服务
		go process(conn)
	}

}
