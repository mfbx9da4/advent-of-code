from dataclasses import dataclass
# David's input
input = """
R 4 (#185fd2)
U 10 (#b6aa53)
L 4 (#5cdb02)
U 3 (#b6aa51)
L 4 (#530592)
U 5 (#65a913)
L 2 (#051d62)
U 6 (#153e33)
L 4 (#3f1372)
D 4 (#9095e3)
L 10 (#3f1370)
D 6 (#58c163)
R 5 (#7850b2)
D 2 (#28f7f1)
R 4 (#3f0392)
D 9 (#743623)
R 4 (#34f1f2)
D 7 (#899b13)
L 4 (#95ffa2)
D 6 (#899b11)
L 9 (#57ac62)
D 3 (#86c073)
L 4 (#0b4b92)
U 4 (#0d1711)
L 4 (#1cc472)
U 5 (#be33a1)
L 6 (#1cc470)
U 4 (#2fabe1)
L 6 (#290df2)
U 9 (#28f7f3)
L 6 (#17a9f2)
U 2 (#450843)
L 10 (#21ad12)
U 3 (#2f46a3)
R 8 (#8debe2)
U 3 (#4bede3)
R 5 (#3affd2)
U 4 (#5bbe23)
R 9 (#131872)
U 3 (#5712a3)
L 5 (#3ae040)
U 3 (#33c033)
L 7 (#52e450)
U 4 (#7e71b3)
R 6 (#444d50)
U 5 (#20ea63)
R 6 (#9571f0)
U 2 (#9f5c11)
R 4 (#368710)
U 5 (#0f5ca3)
R 5 (#1b8710)
U 3 (#3014c3)
L 5 (#0c2610)
U 5 (#0591d3)
R 5 (#964490)
U 3 (#597ac3)
R 5 (#1da130)
D 3 (#3731b3)
R 3 (#0df070)
D 8 (#2a3db3)
R 4 (#0936c0)
U 6 (#3e59a1)
R 3 (#146fe2)
U 5 (#608691)
R 7 (#146fe0)
U 7 (#51b081)
R 3 (#0a0a30)
U 5 (#5329d3)
L 8 (#4d41b0)
U 4 (#c3abc3)
L 3 (#5b0fa0)
U 4 (#216e53)
L 2 (#58f470)
U 7 (#a49b53)
R 10 (#54efb0)
U 2 (#27c9e3)
L 10 (#22dc80)
U 6 (#6af783)
L 7 (#4590f0)
U 6 (#398293)
L 5 (#4590f2)
D 4 (#9b27e3)
L 2 (#23ff42)
D 9 (#822a73)
L 5 (#23ff40)
D 3 (#11cd93)
L 2 (#ad67c2)
D 10 (#6ffb73)
L 7 (#2001e2)
D 3 (#356fe3)
L 4 (#485f62)
U 7 (#4d4103)
L 8 (#5d7130)
U 6 (#020903)
L 3 (#37cc32)
U 5 (#7cb833)
L 5 (#37cc30)
D 5 (#73ad53)
L 4 (#6337e0)
D 6 (#6b0281)
L 3 (#0d8452)
U 11 (#5d1e21)
L 3 (#0d8450)
D 4 (#2a4de1)
L 5 (#551ff0)
D 5 (#37e513)
L 3 (#685900)
D 9 (#1d9d01)
L 3 (#103ec0)
U 9 (#52c7a1)
L 3 (#3525f2)
U 2 (#6ccdd1)
L 4 (#3525f0)
U 9 (#049991)
L 8 (#670f40)
U 4 (#1fc543)
R 4 (#6554b2)
U 6 (#69c9b3)
R 4 (#01e560)
U 6 (#2977c3)
R 7 (#01e562)
U 3 (#517d43)
R 11 (#6554b0)
U 6 (#200223)
R 8 (#0743a0)
U 8 (#2c3ca3)
R 4 (#190d00)
U 8 (#266011)
R 4 (#73fd30)
U 8 (#7b4b31)
R 3 (#492cd0)
U 4 (#4fff11)
R 5 (#9e1f20)
U 6 (#5f1861)
R 2 (#489440)
U 2 (#28f5a3)
R 5 (#36a720)
U 3 (#b8d663)
R 7 (#51ce60)
U 5 (#480693)
R 6 (#1ae5f0)
U 4 (#0972a3)
R 5 (#b54870)
D 4 (#0972a1)
R 8 (#175720)
U 4 (#480691)
R 5 (#0b55d0)
U 6 (#7e1633)
R 7 (#968ee2)
U 9 (#02ec63)
R 2 (#27cc00)
U 10 (#0d0613)
R 3 (#6d6f40)
U 5 (#0d0611)
R 10 (#3eeae0)
D 3 (#1c4293)
L 5 (#0ef560)
D 7 (#2e6c53)
L 5 (#9cd4f2)
D 11 (#6ada23)
R 5 (#9cd4f0)
D 4 (#4db983)
R 5 (#151be0)
D 4 (#21f9c3)
R 8 (#205bc2)
D 4 (#36ab51)
R 6 (#a20722)
U 8 (#36ab53)
L 5 (#35d482)
U 11 (#2ed133)
R 5 (#723852)
U 5 (#134f63)
L 5 (#1b4082)
U 3 (#575003)
R 5 (#b739f2)
U 4 (#16d793)
R 5 (#0d0642)
U 2 (#8d4163)
R 7 (#8080f2)
D 7 (#47e6c3)
R 6 (#390742)
D 9 (#5e0ce3)
L 8 (#b98830)
D 7 (#72baa3)
R 8 (#80b432)
D 8 (#0c6133)
R 3 (#187e62)
U 3 (#573d13)
R 3 (#c327d2)
U 6 (#573d11)
R 7 (#2444c2)
U 4 (#157c83)
L 4 (#92b8d2)
U 3 (#200c93)
L 5 (#457272)
U 7 (#027273)
R 3 (#a1e732)
U 7 (#083993)
R 6 (#47d112)
U 4 (#a93863)
R 4 (#04d492)
U 2 (#6d7973)
R 6 (#a38da0)
D 5 (#1323b3)
R 6 (#117310)
D 3 (#2113c3)
R 4 (#6c8140)
D 5 (#9db833)
L 4 (#710bd0)
D 4 (#0a8b73)
L 6 (#4b16c0)
D 9 (#031c13)
L 7 (#2fdeb0)
D 3 (#2556b3)
R 4 (#558ef0)
D 4 (#0c4823)
R 4 (#3f8970)
D 8 (#96b223)
R 3 (#828d60)
U 4 (#1da791)
R 2 (#01d990)
U 8 (#3289f1)
R 4 (#b6ed00)
D 7 (#55ce81)
R 6 (#6054f0)
U 10 (#82a943)
L 6 (#8c81e0)
U 5 (#2356c3)
R 6 (#2a57d0)
U 9 (#7d8313)
R 2 (#04b760)
U 7 (#0f9583)
R 5 (#8e74b0)
U 6 (#58f5f3)
R 8 (#700842)
D 6 (#6542a3)
R 3 (#2323d2)
U 6 (#065ee3)
R 10 (#3a80f0)
U 4 (#82cbc3)
R 10 (#53c160)
U 2 (#4e4a43)
R 2 (#c00090)
U 6 (#41db93)
R 7 (#0027e0)
U 5 (#9025d1)
R 3 (#3faf50)
D 5 (#75ccf1)
R 6 (#9b4870)
D 5 (#597e03)
R 3 (#4ddd22)
D 10 (#5cfda3)
R 6 (#4ddd20)
D 11 (#952873)
R 4 (#5d49f2)
D 5 (#01da53)
R 7 (#5f2932)
D 10 (#b9f063)
R 5 (#1fa7d0)
D 8 (#4666c3)
R 3 (#9ccb50)
D 3 (#769c93)
R 5 (#1fe970)
D 7 (#144e01)
R 4 (#798f60)
D 7 (#3ec073)
L 4 (#3569f0)
D 8 (#94c3f3)
R 4 (#747dd0)
D 5 (#20d6d3)
R 7 (#077540)
D 3 (#254691)
R 4 (#495f10)
D 2 (#434111)
R 4 (#2e51f0)
U 4 (#8bd391)
R 6 (#30bf90)
U 4 (#b02ad1)
R 4 (#5c3450)
D 4 (#478d41)
R 6 (#5da972)
U 7 (#904281)
R 6 (#54e912)
U 3 (#2ac801)
L 4 (#209b32)
U 3 (#445131)
L 9 (#726c32)
U 3 (#445133)
L 6 (#4ac932)
U 9 (#2ac803)
L 3 (#155922)
U 6 (#2d8331)
R 8 (#89d512)
D 3 (#97ff31)
R 5 (#312010)
D 2 (#062981)
R 5 (#0e0a80)
D 7 (#5b0221)
R 8 (#8b68d0)
D 2 (#5b0223)
R 4 (#4dda80)
D 3 (#062983)
R 4 (#4acf40)
D 8 (#62a721)
R 2 (#31ef70)
D 6 (#82c8e3)
L 5 (#69d920)
D 8 (#82c8e1)
L 6 (#631940)
D 4 (#3a7881)
L 5 (#45e4f0)
D 5 (#5dc8c1)
R 4 (#ab2bc0)
D 5 (#5dc8c3)
L 4 (#0e37c0)
D 5 (#b73991)
L 5 (#65f6d0)
U 3 (#b73993)
L 7 (#66d670)
U 4 (#687961)
R 7 (#6176a0)
U 5 (#98c8a1)
L 3 (#3dedc0)
U 3 (#319cf1)
L 5 (#285a10)
U 4 (#33a483)
L 6 (#5b47e0)
D 9 (#96c113)
R 4 (#2de480)
D 8 (#8c8d81)
L 3 (#019d20)
U 4 (#ab8881)
L 8 (#175860)
D 4 (#51da61)
L 8 (#4023f0)
D 7 (#523121)
R 7 (#349840)
D 5 (#a08b91)
R 6 (#7dd070)
D 4 (#5d8601)
R 3 (#7cf760)
U 9 (#0c26f1)
R 3 (#2a7d30)
D 5 (#82e861)
R 5 (#3e46c0)
D 10 (#2f8121)
R 7 (#55f470)
U 8 (#4b1a31)
R 2 (#1bb7c0)
U 5 (#63b3d1)
R 5 (#007722)
U 2 (#3f3a81)
R 4 (#007720)
U 7 (#4d03a1)
R 2 (#29ee20)
U 8 (#175c81)
R 3 (#086db0)
D 3 (#1d6631)
R 3 (#9b9da0)
D 11 (#959c71)
R 5 (#465862)
U 3 (#8df221)
R 6 (#2a2642)
U 5 (#601fb1)
L 6 (#146a62)
U 5 (#99e261)
R 2 (#9524f2)
U 4 (#35b8a1)
R 7 (#05bcf2)
U 4 (#74cfe1)
R 9 (#122a82)
U 7 (#283ec1)
R 5 (#98a4e2)
D 5 (#4e9363)
R 6 (#2a4b92)
D 4 (#3c9093)
R 6 (#7f7b02)
U 2 (#ac7ce3)
R 3 (#7f7b00)
U 7 (#266ad3)
R 6 (#2a4b90)
D 5 (#528973)
R 5 (#6b7e32)
D 5 (#0a92d3)
R 4 (#c3b802)
U 5 (#352e03)
R 6 (#bf7462)
D 3 (#65cfb3)
R 4 (#8c2af2)
D 3 (#0495e3)
R 3 (#832dd2)
D 10 (#022e51)
R 7 (#07c5d2)
D 4 (#041c01)
R 10 (#26ed22)
D 3 (#b00f91)
R 6 (#66d172)
D 3 (#6f4921)
R 6 (#888172)
D 11 (#10de41)
R 3 (#1ae2a2)
D 7 (#243b83)
R 6 (#1be9f0)
D 5 (#5874b3)
L 6 (#06ae32)
D 10 (#207c23)
L 7 (#06ae30)
D 9 (#4ca443)
L 4 (#1be9f2)
U 9 (#4cb0b3)
L 4 (#1e0de2)
U 10 (#5cb0a1)
L 5 (#2e4fb2)
U 8 (#705f51)
L 3 (#b41bc2)
U 4 (#7c63f1)
L 7 (#901670)
U 9 (#0c7fa1)
L 4 (#240550)
U 4 (#5f23d1)
L 5 (#58a592)
D 4 (#152b71)
L 10 (#58a590)
D 2 (#5af221)
L 3 (#5a1fe0)
D 9 (#82c2b1)
R 7 (#a3fca0)
D 9 (#45bd61)
L 7 (#144cc0)
D 9 (#a38ef1)
L 7 (#4bd0d0)
D 4 (#6fbe01)
L 3 (#983b90)
D 7 (#394ea1)
L 7 (#6a8f70)
U 9 (#638b63)
L 3 (#b84420)
U 7 (#458143)
L 3 (#1f79e0)
D 3 (#a6c921)
L 4 (#218680)
D 5 (#16b981)
L 2 (#453fe0)
D 10 (#608851)
L 3 (#5973f0)
U 5 (#5591d1)
L 8 (#7647b0)
U 2 (#3c2cd1)
R 8 (#3ed7b2)
U 5 (#3df061)
L 4 (#90e3f2)
U 6 (#226a71)
L 3 (#453fe2)
D 7 (#910ce1)
L 5 (#0782e0)
D 4 (#3fdca1)
L 6 (#787f72)
D 8 (#3faa51)
L 4 (#3f8002)
D 3 (#67ebc3)
L 2 (#6b6672)
D 9 (#402f81)
L 4 (#47d1b2)
D 9 (#a110f1)
L 2 (#5693d0)
D 3 (#998b41)
L 5 (#5693d2)
D 3 (#556501)
L 10 (#47d1b0)
D 6 (#51cc51)
R 10 (#8b8ab2)
D 3 (#00e693)
L 2 (#1ac042)
D 3 (#0f57c3)
L 2 (#1348f2)
D 6 (#c0c063)
L 4 (#1348f0)
D 3 (#042dd3)
L 4 (#0d24f2)
D 9 (#5f4103)
L 7 (#3ed3c2)
D 2 (#3e1d23)
L 4 (#181272)
U 11 (#ae42f3)
L 3 (#8585d2)
U 2 (#012f73)
L 4 (#305e92)
D 8 (#67ebc1)
L 3 (#240c42)
D 5 (#6b0ba1)
L 5 (#4aa9a2)
U 5 (#215963)
L 3 (#2960e2)
U 6 (#bba0d3)
L 5 (#579652)
U 5 (#45b791)
L 4 (#53f582)
U 10 (#883c81)
L 4 (#53f580)
U 5 (#0f0621)
R 9 (#302402)
U 3 (#25f621)
L 9 (#7dd240)
U 4 (#06a081)
L 2 (#a51cf0)
U 4 (#556b01)
L 5 (#222ef0)
U 4 (#2945e1)
L 3 (#862360)
U 6 (#8e5051)
L 7 (#55d172)
D 6 (#70b7b1)
L 3 (#6d8f32)
U 6 (#c1d1d1)
L 4 (#0d7442)
U 3 (#03cf71)
R 9 (#0ee642)
U 4 (#1c5e23)
R 7 (#160452)
U 6 (#b57503)
L 6 (#160450)
U 2 (#6485d3)
L 5 (#600a62)
U 6 (#090a91)
L 5 (#478692)
U 3 (#0bc7b1)
L 4 (#821af2)
D 2 (#69ccf1)
L 9 (#821af0)
D 8 (#4ec5b1)
L 8 (#399ca2)
D 8 (#0f7e41)
L 5 (#0a58d2)
D 6 (#1b28d1)
L 11 (#6fab02)
D 3 (#3267b1)
R 7 (#5a1742)
D 3 (#51a271)
R 4 (#12cfc0)
D 4 (#17e2b3)
L 5 (#1522b0)
D 5 (#373ee1)
R 4 (#9a7000)
U 2 (#373ee3)
R 6 (#17ca10)
U 8 (#17e2b1)
R 7 (#05b8b0)
D 4 (#8e8ea1)
R 3 (#11e000)
D 6 (#24b8e1)
R 3 (#84f220)
D 5 (#05baf1)
L 4 (#60fa82)
D 5 (#691b81)
L 5 (#31bf92)
D 3 (#5ff001)
R 8 (#73a822)
D 6 (#61b511)
R 3 (#5f3e20)
D 3 (#358521)
L 3 (#5de030)
D 6 (#8f1391)
L 8 (#4943e0)
D 4 (#9b41e1)
L 4 (#16a272)
U 9 (#1a1601)
L 5 (#3a5d12)
U 5 (#95ede1)
R 5 (#579db2)
U 4 (#295691)
L 5 (#4e92d2)
U 4 (#41ad01)
L 5 (#7f8752)
D 8 (#07aeb1)
L 6 (#32de52)
D 5 (#559a73)
L 9 (#9bffa2)
D 2 (#56f793)
L 3 (#bc5802)
U 5 (#605113)
L 9 (#77c880)
U 8 (#3494a3)
L 9 (#0e2d90)
U 8 (#a52503)
R 7 (#0e2d92)
U 6 (#050f83)
L 7 (#5f6800)
U 6 (#474531)
L 7 (#471ff0)
U 6 (#145321)
L 5 (#5770f0)
U 4 (#8330d1)
R 3 (#019e30)
U 4 (#b32b93)
R 6 (#8293f0)
D 4 (#305133)
R 5 (#316ad2)
U 4 (#865e83)
R 4 (#6489c2)
D 4 (#5890c3)
R 3 (#7276d2)
U 7 (#42c2d3)
L 6 (#8e0cb2)
U 6 (#696303)
L 4 (#637b72)
U 3 (#401103)
L 3 (#324492)
U 5 (#b686e3)
L 4 (#1befb2)
U 5 (#6c04c3)
L 3 (#201172)
U 9 (#3717a1)
L 4 (#7eb7b2)
D 10 (#9a97f1)
L 7 (#72fb12)
D 4 (#50dc11)
L 7 (#16a842)
D 5 (#156ec3)
L 2 (#13d402)
D 2 (#735093)
L 3 (#8a1ae2)
U 6 (#735091)
L 4 (#54de72)
D 6 (#2b32a3)
L 6 (#4611e0)
D 3 (#762253)
R 5 (#59e090)
D 7 (#389f93)
L 4 (#70ab50)
D 3 (#166283)
L 3 (#247e92)
D 8 (#91ca63)
R 6 (#9ddeb2)
D 6 (#1f7f03)
R 3 (#4e4082)
D 7 (#697043)
R 5 (#c308e2)
U 11 (#21c073)
R 5 (#13fef2)
D 11 (#a06563)
R 6 (#61b5d2)
D 3 (#1cd9c3)
R 2 (#4f0852)
D 3 (#60fcc3)
L 6 (#98bf82)
D 7 (#214541)
L 9 (#6688f0)
U 4 (#80bad1)
L 2 (#621f30)
U 3 (#9b27a1)
L 10 (#621f32)
D 3 (#6aa341)
R 7 (#4da592)
D 5 (#a3edf1)
L 11 (#91d450)
D 5 (#880101)
L 5 (#0fdba0)
D 5 (#339fe1)
R 8 (#a1aff2)
D 3 (#8766f1)
R 8 (#4da590)
D 4 (#32d0e1)
L 5 (#6688f2)
D 4 (#53a7c1)
L 4 (#084142)
D 3 (#19c573)
L 4 (#686872)
D 9 (#35f161)
L 3 (#8a3bf2)
U 7 (#35f163)
L 2 (#00f612)
U 5 (#1d9613)
L 7 (#215cf2)
U 5 (#8ef363)
L 3 (#152312)
U 6 (#298013)
"""

# Leandro's input
# input = """
# L 4 (#0527c0)
# U 6 (#3bb5c3)
# L 3 (#916d22)
# U 4 (#504aa3)
# L 3 (#916d20)
# U 2 (#1902a3)
# L 8 (#0527c2)
# U 6 (#1acd53)
# L 6 (#23be82)
# U 7 (#748693)
# L 3 (#2082a2)
# D 2 (#43e263)
# L 4 (#674a82)
# D 3 (#43e261)
# L 2 (#50d992)
# D 7 (#24b3e3)
# L 4 (#383df2)
# D 5 (#33b883)
# L 8 (#28f582)
# D 5 (#33bf63)
# L 5 (#64c212)
# D 3 (#6097c3)
# L 3 (#8db790)
# U 6 (#1ee6b3)
# L 3 (#23bca2)
# U 5 (#118043)
# L 8 (#1d9c12)
# U 3 (#17eb01)
# L 3 (#7c8502)
# U 6 (#6c4391)
# L 7 (#789232)
# U 6 (#64a371)
# L 8 (#76f482)
# U 6 (#1a8393)
# L 6 (#1fca22)
# U 6 (#16dfa3)
# L 8 (#718620)
# U 5 (#519e23)
# R 5 (#14cc30)
# U 9 (#2b7a53)
# R 6 (#865252)
# D 5 (#3a5663)
# R 5 (#055462)
# D 2 (#12f1e3)
# R 4 (#66eb00)
# D 6 (#7bbe93)
# R 4 (#4caeb2)
# U 6 (#071323)
# R 2 (#3be932)
# U 7 (#071321)
# R 6 (#410472)
# U 3 (#725a63)
# L 6 (#327b32)
# U 7 (#210cc1)
# L 5 (#4fed22)
# U 3 (#056631)
# L 6 (#4330e0)
# U 5 (#57ae61)
# L 6 (#4feb60)
# U 5 (#4cdda1)
# L 2 (#4feb62)
# U 4 (#1b4091)
# L 3 (#4330e2)
# U 3 (#0a71d1)
# L 3 (#3614b2)
# U 3 (#43d973)
# L 7 (#623d60)
# U 2 (#33a743)
# L 4 (#623d62)
# U 3 (#5823e3)
# L 4 (#5fe6c2)
# U 10 (#210cc3)
# L 3 (#0edfe2)
# U 4 (#8b3493)
# L 10 (#190480)
# U 5 (#121a33)
# R 10 (#86a0a0)
# U 4 (#5747e3)
# L 5 (#726770)
# U 6 (#22c5e3)
# R 2 (#34a340)
# U 4 (#558f31)
# R 4 (#44dad0)
# U 4 (#558f33)
# R 4 (#655550)
# U 10 (#909e53)
# R 4 (#2e4f50)
# D 3 (#278683)
# R 4 (#233f50)
# D 6 (#0e2e31)
# R 4 (#897c40)
# D 5 (#2c1101)
# R 4 (#83ced0)
# U 7 (#137751)
# R 6 (#2ce220)
# U 3 (#033061)
# R 4 (#43f060)
# U 7 (#88ef11)
# R 5 (#53a110)
# U 3 (#54e4a1)
# L 3 (#071630)
# U 4 (#2c6721)
# L 6 (#2f70e2)
# U 3 (#2f03f1)
# L 6 (#2006b2)
# U 5 (#3b8843)
# R 8 (#3f35b2)
# U 4 (#00d131)
# R 3 (#441e92)
# U 4 (#00d133)
# R 4 (#0e74c2)
# U 4 (#3b8841)
# R 9 (#3ba1a2)
# D 4 (#2f03f3)
# R 7 (#337852)
# U 4 (#3a1571)
# R 7 (#2c9750)
# U 4 (#642601)
# R 4 (#6181b0)
# U 3 (#7a7771)
# R 3 (#46d2f0)
# U 9 (#7a7773)
# L 2 (#0b86f0)
# U 6 (#6ea261)
# L 5 (#5ed550)
# U 5 (#244121)
# R 10 (#111250)
# D 3 (#3159a1)
# R 6 (#726be0)
# D 2 (#5de773)
# R 6 (#036bb0)
# D 3 (#4df7d3)
# R 5 (#6831b0)
# D 4 (#2d1233)
# R 6 (#6b9820)
# D 4 (#4ff453)
# L 10 (#08b5d0)
# D 3 (#879323)
# L 5 (#63fb10)
# D 5 (#0f13b3)
# L 8 (#0360c0)
# D 3 (#0d2a53)
# R 4 (#4067e0)
# D 3 (#8d8511)
# R 9 (#430ff0)
# D 4 (#8d8513)
# R 4 (#2ddeb0)
# D 6 (#453fb3)
# R 6 (#27fc00)
# D 6 (#71bde3)
# L 4 (#4dab60)
# D 6 (#149ad3)
# L 9 (#0c98b0)
# D 3 (#447361)
# R 7 (#47bb40)
# D 6 (#601771)
# R 4 (#47bb42)
# D 2 (#040c91)
# R 2 (#545370)
# D 5 (#1d69c3)
# R 4 (#638900)
# D 3 (#437033)
# R 6 (#638902)
# U 5 (#47bd73)
# R 5 (#5f2ab0)
# U 7 (#49c933)
# R 2 (#0bb8b0)
# U 3 (#40b0c3)
# R 4 (#1b90a0)
# U 6 (#6661a3)
# L 6 (#562ca0)
# U 4 (#133703)
# R 6 (#6f0ca0)
# U 3 (#42d963)
# R 3 (#4928c0)
# U 3 (#134293)
# L 9 (#8e1fd0)
# U 6 (#5facf3)
# R 6 (#254850)
# U 4 (#2ce993)
# R 4 (#254852)
# U 6 (#5d1303)
# R 3 (#1abd42)
# U 8 (#0a56e3)
# R 3 (#519432)
# D 10 (#4e47a3)
# R 5 (#38ade2)
# D 4 (#85f063)
# R 3 (#3ac2c2)
# D 7 (#85f061)
# R 3 (#1e28c2)
# U 7 (#2d0573)
# R 6 (#1c3492)
# U 4 (#7e36d3)
# L 6 (#5139e2)
# U 9 (#1c1ae3)
# R 4 (#3816f2)
# U 3 (#620271)
# R 4 (#7e5fd2)
# U 2 (#0fa081)
# R 4 (#1dc272)
# D 2 (#2de883)
# R 2 (#0766e2)
# D 8 (#76f7a3)
# R 5 (#621722)
# D 9 (#2328c1)
# R 5 (#3d21c2)
# D 6 (#81b761)
# R 8 (#1a1372)
# D 5 (#71a2f3)
# L 4 (#4fec02)
# D 6 (#110563)
# L 6 (#535812)
# D 3 (#110561)
# L 5 (#258812)
# D 6 (#026923)
# L 3 (#039992)
# D 4 (#049f03)
# L 3 (#487782)
# D 4 (#8c4e63)
# L 2 (#2e40f2)
# D 7 (#0d4873)
# L 3 (#254702)
# D 3 (#30a1c3)
# L 7 (#0543b2)
# U 7 (#161661)
# R 4 (#2d03d2)
# U 8 (#6bd3a1)
# L 4 (#2d03d0)
# U 9 (#4ced91)
# L 5 (#5c5202)
# D 7 (#6ad1f3)
# L 5 (#247ad2)
# D 10 (#2b7b43)
# L 5 (#3cc600)
# D 6 (#25d953)
# L 3 (#549232)
# D 4 (#43c7c3)
# L 3 (#549230)
# U 4 (#339163)
# L 5 (#049e70)
# D 4 (#27b3d3)
# L 7 (#884440)
# U 4 (#4066b3)
# L 3 (#436100)
# D 4 (#26d613)
# L 4 (#3077a0)
# D 4 (#1ca153)
# R 6 (#0930a0)
# D 5 (#6ed8f3)
# R 5 (#00c0c2)
# D 2 (#15bfc1)
# R 7 (#2a7622)
# D 3 (#581721)
# R 3 (#6134a2)
# D 6 (#28cf83)
# R 9 (#3145e2)
# D 3 (#450763)
# L 4 (#1045b2)
# D 3 (#77dd33)
# L 8 (#1d0160)
# D 6 (#4401a3)
# L 3 (#83f0b0)
# D 6 (#4401a1)
# L 9 (#2d0500)
# D 3 (#1f11e3)
# L 6 (#259800)
# D 5 (#0da373)
# L 7 (#8f57c0)
# D 4 (#0bf321)
# L 11 (#691c32)
# D 3 (#591231)
# R 12 (#08f572)
# D 4 (#5f59b1)
# R 6 (#08f570)
# D 6 (#61c371)
# R 7 (#4792e2)
# D 3 (#09b171)
# L 9 (#4bee90)
# D 2 (#688c13)
# L 2 (#2fb0c0)
# D 4 (#688c11)
# L 7 (#350fc0)
# D 2 (#270ef1)
# L 5 (#45a2d0)
# D 4 (#1a7e91)
# R 4 (#120162)
# D 2 (#31cbc1)
# R 7 (#2f2c80)
# D 4 (#2ee8c1)
# R 3 (#2f2c82)
# D 3 (#6040a1)
# R 9 (#120160)
# D 3 (#29d941)
# R 11 (#0fa8b0)
# U 4 (#1bdfc3)
# R 5 (#35b2e0)
# U 4 (#1eea81)
# L 5 (#6fec70)
# U 5 (#1eea83)
# R 5 (#187e70)
# U 5 (#03a4c3)
# L 5 (#3f4ba0)
# U 3 (#31d223)
# R 3 (#785fd0)
# U 6 (#75e933)
# R 6 (#50d780)
# D 6 (#67c7c3)
# R 5 (#47e270)
# D 4 (#06be13)
# R 10 (#385c60)
# U 4 (#479bf3)
# R 7 (#197b82)
# D 5 (#197f63)
# L 3 (#197b80)
# D 2 (#47ec03)
# L 7 (#4264e0)
# D 4 (#16ce63)
# L 8 (#2c3760)
# D 2 (#057583)
# L 4 (#45f380)
# D 5 (#8cffd3)
# R 3 (#45f382)
# D 3 (#1e1e03)
# R 5 (#50c272)
# D 6 (#366961)
# R 3 (#7d6272)
# D 2 (#366963)
# R 6 (#68f242)
# D 10 (#2c7df3)
# R 4 (#06f1f0)
# D 3 (#059771)
# R 7 (#6cd650)
# U 7 (#059773)
# R 3 (#214570)
# U 4 (#0b5493)
# R 3 (#7d2870)
# U 3 (#0b5491)
# R 6 (#24e100)
# U 3 (#16f7d3)
# R 6 (#452280)
# U 3 (#5690b3)
# R 6 (#520b00)
# U 4 (#358943)
# R 6 (#373670)
# D 4 (#732373)
# R 3 (#0aa860)
# U 6 (#3d68c3)
# R 6 (#517b62)
# U 4 (#429e93)
# R 10 (#620632)
# U 3 (#09d7b3)
# R 2 (#1acaf2)
# U 6 (#02d973)
# R 7 (#2e65c0)
# U 4 (#43f143)
# R 3 (#384210)
# U 7 (#1d6af3)
# R 2 (#384212)
# U 7 (#35d3b3)
# R 2 (#4e6b60)
# U 7 (#2c3ab3)
# R 6 (#517b60)
# U 2 (#6c60f3)
# R 4 (#1f5430)
# U 7 (#5462a3)
# R 5 (#80b160)
# U 9 (#48e5f3)
# R 4 (#255fe0)
# U 2 (#07e8d1)
# R 4 (#315950)
# U 6 (#5c7051)
# R 6 (#315952)
# U 5 (#38ef71)
# L 2 (#0c3b50)
# U 3 (#335201)
# L 6 (#6c7bb0)
# U 2 (#33cdb3)
# L 6 (#5593d0)
# U 4 (#3f2fc3)
# R 11 (#5593d2)
# U 3 (#2e2443)
# R 6 (#34d5c0)
# U 4 (#181b43)
# R 4 (#3a9ee0)
# D 7 (#4aa921)
# R 8 (#0356c2)
# D 5 (#13f461)
# L 5 (#0356c0)
# D 2 (#5a9f71)
# L 5 (#454b60)
# D 5 (#686aa1)
# R 4 (#6d6f10)
# D 3 (#4ab481)
# R 3 (#466640)
# D 9 (#7cc693)
# L 3 (#798b50)
# D 2 (#1b8fb3)
# L 4 (#10ea50)
# D 4 (#3edc83)
# R 2 (#212530)
# D 7 (#46c5d3)
# R 8 (#212532)
# D 4 (#0d5693)
# R 5 (#3b5940)
# D 3 (#1a5ff1)
# L 2 (#887140)
# D 5 (#670211)
# L 3 (#887142)
# U 4 (#1196e1)
# L 5 (#606960)
# D 4 (#134651)
# L 5 (#3b5f20)
# D 6 (#787031)
# R 3 (#3b5f22)
# D 5 (#0c9fc1)
# R 3 (#407a30)
# D 7 (#051701)
# R 3 (#149010)
# U 3 (#69b091)
# R 3 (#813cd2)
# U 9 (#109f81)
# R 3 (#161b70)
# D 5 (#41c011)
# R 4 (#6b2160)
# D 4 (#343c71)
# R 6 (#149012)
# D 3 (#0a12e1)
# R 4 (#581f80)
# U 11 (#522261)
# R 2 (#7874d0)
# U 4 (#373d41)
# R 6 (#2f19a2)
# U 5 (#3e35a1)
# R 2 (#0de102)
# U 6 (#456551)
# R 4 (#0de100)
# D 3 (#2465c1)
# R 4 (#0f1b42)
# D 9 (#0a4c71)
# L 4 (#5393c2)
# D 8 (#2ae8a3)
# R 3 (#18ea12)
# D 5 (#5394f3)
# R 3 (#18ea10)
# U 6 (#1fb183)
# R 7 (#1d0762)
# U 5 (#141e13)
# R 3 (#5673b2)
# U 10 (#2ec1a3)
# R 4 (#1a1bb2)
# U 3 (#70ed53)
# R 3 (#52db22)
# D 13 (#04f2a3)
# R 3 (#51a8a2)
# U 6 (#3360a3)
# R 7 (#128552)
# D 4 (#61a5d3)
# R 4 (#501472)
# D 5 (#0c2111)
# R 5 (#0dcd62)
# U 9 (#0c2113)
# R 6 (#4d9bd2)
# U 3 (#4a18c3)
# R 4 (#0f6ce2)
# D 8 (#862351)
# L 5 (#2944d2)
# D 7 (#720fe1)
# R 5 (#1bf2a2)
# D 5 (#647593)
# R 3 (#5e6c02)
# D 3 (#48a7e3)
# L 7 (#2a7542)
# D 7 (#19c801)
# L 2 (#77d322)
# D 4 (#46c981)
# L 5 (#77d320)
# D 5 (#4c8bf1)
# L 9 (#0a1912)
# D 3 (#4591d1)
# L 7 (#0b5680)
# U 4 (#211b01)
# L 4 (#019ce0)
# U 8 (#61b6c3)
# L 4 (#481b60)
# U 3 (#8a7821)
# L 3 (#16eee0)
# D 11 (#8a7823)
# L 4 (#3ba830)
# U 4 (#61b6c1)
# L 4 (#1b5fc0)
# D 5 (#211b03)
# L 3 (#152c30)
# D 2 (#45fbc1)
# L 3 (#59c922)
# D 11 (#56f791)
# R 4 (#30dd80)
# D 6 (#193741)
# R 6 (#4ca810)
# U 5 (#193743)
# R 8 (#278d90)
# D 5 (#003271)
# R 5 (#087900)
# D 3 (#1f7121)
# L 9 (#726832)
# D 3 (#473e31)
# L 5 (#2c0442)
# D 4 (#28ae11)
# L 7 (#0f1fb2)
# D 3 (#0c8a31)
# R 6 (#51bdd0)
# D 5 (#8329b1)
# R 10 (#5f8530)
# D 3 (#6ac303)
# R 5 (#5abb90)
# D 6 (#6ac301)
# L 4 (#25bbd0)
# D 4 (#6036f1)
# L 7 (#02f992)
# D 6 (#3294f1)
# L 6 (#7627f2)
# U 8 (#4a9d11)
# L 3 (#46d412)
# U 2 (#1a1d21)
# L 4 (#4fe262)
# D 5 (#420241)
# L 9 (#50d7b0)
# D 5 (#47fe91)
# L 4 (#556f00)
# U 8 (#47fe93)
# L 5 (#699140)
# U 3 (#865af1)
# L 3 (#090010)
# D 11 (#239fd1)
# L 3 (#1acfe2)
# D 4 (#821781)
# L 6 (#53a922)
# D 4 (#3ed441)
# R 12 (#1f3002)
# D 2 (#3ed443)
# R 6 (#6e4c42)
# D 5 (#3453f1)
# R 3 (#4204e0)
# D 5 (#5a4501)
# L 8 (#8b7220)
# D 2 (#5a4503)
# L 6 (#1682d0)
# D 4 (#788961)
# L 6 (#17fb70)
# D 7 (#51e0f1)
# L 5 (#170860)
# D 10 (#149871)
# L 2 (#041210)
# D 2 (#0cc641)
# L 4 (#271030)
# D 3 (#120c41)
# R 4 (#542090)
# D 3 (#822fb1)
# R 6 (#5ded30)
# D 4 (#7a0531)
# R 6 (#5d7270)
# U 2 (#8502c1)
# R 3 (#64f120)
# U 3 (#574831)
# L 4 (#650f70)
# U 2 (#2f8f81)
# L 2 (#51caf2)
# U 9 (#3fde61)
# R 6 (#51caf0)
# U 8 (#6c2f51)
# R 5 (#17fab2)
# D 10 (#315101)
# R 5 (#8cb680)
# D 2 (#5733e1)
# R 5 (#047f00)
# D 7 (#308f11)
# R 2 (#137e10)
# D 5 (#08f7f1)
# R 4 (#2e3610)
# D 7 (#17f511)
# R 6 (#47ace2)
# D 6 (#30c5f1)
# L 6 (#622732)
# D 5 (#2d7891)
# L 6 (#291592)
# U 4 (#51ee41)
# L 12 (#7a8902)
# U 4 (#48e8b1)
# L 12 (#268482)
# U 2 (#830fd3)
# L 3 (#4e33c2)
# U 3 (#2b2e93)
# L 3 (#38dee2)
# U 2 (#4de931)
# L 8 (#7ea022)
# U 3 (#172c81)
# L 8 (#7ea020)
# D 7 (#4928b1)
# L 5 (#66c0b2)
# U 7 (#624791)
# L 4 (#74cfe2)
# U 5 (#254451)
# L 4 (#6bf3e0)
# U 3 (#856f61)
# L 3 (#457980)
# U 4 (#1389c1)
# R 5 (#5ded02)
# U 4 (#6aa501)
# R 3 (#538062)
# D 8 (#4834f1)
# R 4 (#327b22)
# D 4 (#4bc593)
# R 3 (#5c0892)
# U 9 (#20bb93)
# R 4 (#5b5032)
# U 3 (#63f003)
# R 5 (#4e9992)
# U 5 (#2db793)
# L 3 (#3a0160)
# U 5 (#1057d1)
# L 7 (#3fe690)
# U 3 (#1057d3)
# L 3 (#447de0)
# U 3 (#03f2d3)
# L 5 (#211370)
# U 4 (#495b03)
# L 6 (#6f7032)
# U 4 (#47ae63)
# R 8 (#1c5342)
# U 7 (#079bb3)
# R 2 (#53b5d2)
# U 5 (#204893)
# L 4 (#7646a2)
# U 7 (#698fc3)
# L 6 (#277882)
# U 3 (#3d4223)
# L 5 (#0e4922)
# U 3 (#7f16e3)
# L 8 (#217490)
# U 4 (#045a63)
# L 4 (#598360)
# U 2 (#445401)
# L 7 (#725470)
# U 6 (#339a01)
# L 10 (#409820)
# D 3 (#77ee03)
# L 9 (#2f6170)
# D 4 (#045a61)
# L 2 (#2affe0)
# D 4 (#4ba693)
# L 3 (#707a42)
# D 5 (#5c2923)
# R 6 (#2a0040)
# D 3 (#22cb93)
# R 8 (#5dc130)
# D 4 (#22cb91)
# L 4 (#1e5720)
# D 4 (#44d843)
# L 5 (#26ae62)
# D 4 (#547943)
# L 2 (#7f6a32)
# D 8 (#30ed73)
# L 6 (#3f3ed2)
# D 3 (#0b8e21)
# L 4 (#3a7c22)
# D 6 (#0b8e23)
# L 3 (#1f12e2)
# D 10 (#6882f1)
# L 3 (#424e90)
# D 10 (#5330e1)
# L 2 (#3f2ab2)
# D 2 (#52b8a1)
# L 6 (#3f2ab0)
# U 9 (#089f91)
# L 3 (#424e92)
# U 7 (#0f5c11)
# L 3 (#348422)
# U 4 (#9045b3)
# L 4 (#4a79a2)
# U 6 (#0b1133)
# L 4 (#730882)
# U 4 (#3a83b1)
# R 12 (#15a862)
# U 2 (#0b6db1)
# R 3 (#156530)
# U 4 (#022be1)
# L 4 (#5e7940)
# U 4 (#6869c1)
# L 8 (#0d8702)
# D 4 (#290881)
# L 3 (#665772)
# U 6 (#203041)
# L 3 (#505f02)
# U 3 (#586b23)
# L 3 (#157fa2)
# D 3 (#2141a3)
# L 3 (#8853a2)
# D 8 (#332c81)
# R 6 (#033af2)
# D 6 (#468041)
# L 6 (#4c1062)
# D 6 (#2c2d21)
# L 6 (#22ca82)
# D 3 (#27b411)
# L 7 (#4c73e2)
# D 6 (#4c9e73)
# R 4 (#6b2f10)
# D 10 (#2a4aa3)
# L 4 (#6b2f12)
# D 9 (#4d33d3)
# L 3 (#6615c2)
# D 2 (#3fd0e1)
# L 12 (#4313e2)
# U 4 (#354bf1)
# L 4 (#4313e0)
# U 4 (#4f0011)
# L 4 (#452c52)
# D 12 (#6ba591)
# L 3 (#619750)
# D 4 (#4f4093)
# L 6 (#0dc140)
# U 4 (#1a8633)
# L 7 (#0dc142)
# U 5 (#38a973)
# L 3 (#3671e0)
# U 4 (#2d1e21)
# R 10 (#24e442)
# U 3 (#696c41)
# L 3 (#24e440)
# U 2 (#0be5d1)
# L 2 (#5facc0)
# U 5 (#6e63c1)
# R 4 (#257302)
# U 2 (#123e01)
# R 8 (#062d82)
# U 4 (#6c86b1)
# R 10 (#062d80)
# U 6 (#1427d1)
# L 3 (#257300)
# U 3 (#7e69f1)
# L 4 (#552122)
# U 5 (#8eeea1)
# L 2 (#438402)
# U 6 (#2d1cf1)
# L 3 (#09e402)
# U 7 (#775de1)
# L 5 (#763922)
# U 5 (#361e81)
# L 4 (#1f5982)
# U 10 (#3e7c03)
# R 5 (#257222)
# U 7 (#603b61)
# R 7 (#3d4752)
# D 5 (#603b63)
# R 8 (#5d08b2)
# D 8 (#3e7c01)
# R 8 (#520002)
# U 5 (#4e6b23)
# R 5 (#808930)
# U 3 (#705523)
# R 4 (#808932)
# U 5 (#03a703)
# R 4 (#467562)
# D 6 (#724f73)
# R 4 (#4186b2)
# D 4 (#4244e3)
# R 6 (#7c8152)
# D 4 (#4244e1)
# R 4 (#843402)
# U 10 (#293d71)
# R 2 (#3d72f2)
# U 4 (#207991)
# R 5 (#64b202)
# U 8 (#6faad1)
# L 5 (#053f52)
# U 4 (#6538f1)
# L 7 (#0d2382)
# U 4 (#185833)
# L 6 (#4c2fd2)
# D 8 (#185831)
# L 6 (#4d7af2)
# U 5 (#161bf1)
# L 5 (#1edbc2)
# U 5 (#13c5c3)
# """

# Test input
# input = """
# R 6 (#70c710)
# D 5 (#0dc571)
# L 2 (#5713f0)
# D 2 (#d2c081)
# R 2 (#59c680)
# D 2 (#411b91)
# L 5 (#8ceee2)
# U 2 (#caa173)
# L 1 (#1b58a2)
# U 2 (#caa171)
# R 2 (#7807d2)
# U 3 (#a77fa3)
# L 2 (#015232)
# U 2 (#7a21e3)
# """

# input = """
# R 2 (#000000)
# D 2 (#000000)
# L 2 (#000000)
# U 2 (#000000)
# """

# input = """
# R 2 (#000000)
# U 2 (#000000)
# L 2 (#000000)
# D 2 (#000000)
# """

# input = """
# R 2 (#000000)
# D 2 (#000000)
# L 1 (#000000)
# U 1 (#000000)
# L 1 (#000000)
# U 1 (#000000)
# """

# input = """
# L 2 (#000000)
# U 2 (#000000)
# R 2 (#000000)
# D 2 (#000000)
# """

# Options
# 1. Diagonal
# 2. Flood fill (following left and right of path)
# 3. Green's theorem
# 4. Duplicated everything so that there are no tight walls
# 5. Horizontal traversal


@dataclass(frozen=True)
class Instruction:
    direction: str
    distance: int
    color: str


@dataclass(frozen=True)
class Cell:
    x: int
    y: int


@dataclass(frozen=True)
class Node:
    x: int
    y: int
    directionIn: str
    directionOut: str


instructions = []
for line in input.splitlines():
    if line == "":
        continue
    direction, distance, color = line.split()
    color = color[1:-1]
    instructions.append(Instruction(direction, int(distance), color))

path = [Cell(0, 0)]
bottom_rights_and_top_lefts = set()
prev_instruction = None
for instruction in instructions:
    prev_cell = path[-1]
    x, y = prev_cell.x, prev_cell.y
    if instruction.direction == "R":
        for i in range(instruction.distance):
            path.append(Cell(x + i + 1, y))
    elif instruction.direction == "L":
        for i in range(instruction.distance):
            path.append(Cell(x - i - 1, y))
    elif instruction.direction == "U":
        for i in range(instruction.distance):
            path.append(Cell(x, y - i - 1))
    elif instruction.direction == "D":
        for i in range(instruction.distance):
            path.append(Cell(x, y + i + 1))

    is_bottom_right = (prev_instruction == "D" and instruction.direction == "L") or (
        prev_instruction == "R" and instruction.direction == "U"
    )
    is_top_left = (prev_instruction == "U" and instruction.direction == "R") or (
        prev_instruction == "L" and instruction.direction == "D"
    )
    if is_bottom_right or is_top_left:
        bottom_rights_and_top_lefts.add(prev_cell)

    prev_instruction = instruction.direction

# Account for the first cell being a corner
is_bottom_right = (prev_instruction == "D" and instructions[0].direction == "L") or (
    prev_instruction == "R" and instructions[0].direction == "U"
)
is_top_left = (prev_instruction == "U" and instructions[0].direction == "R") or (
    prev_instruction == "L" and instructions[0].direction == "D"
)
if is_bottom_right or is_top_left:
    bottom_rights_and_top_lefts.add(path[0])

path_as_set = set(path)

path_as_set_without_bottom_rights_and_top_lefts = path_as_set.difference(
    bottom_rights_and_top_lefts
)


min_x = min(cell.x for cell in path) - 1
max_x = max(cell.x for cell in path) + 1
min_y = min(cell.y for cell in path) - 1
max_y = max(cell.y for cell in path) + 1
# bottom and left cells of the board
edge_cells = [Cell(min_x, y) for y in range(min_y, max_y + 1)] + [
    Cell(x, max_y) for x in range(min_x, max_x + 1)
]


def in_bounds(cell):
    return min_x <= cell.x <= max_x and min_y <= cell.y <= max_y


insiders = set()
outsiders = set()
for edge_cell in edge_cells:
    # Create diagonal rays
    state = "out"
    cell = edge_cell
    while in_bounds(cell):
        if state == "in" or cell in path_as_set:
            insiders.add(cell)
        else:
            outsiders.add(cell)
        if cell in path_as_set_without_bottom_rights_and_top_lefts:
            state = "in" if state == "out" else "out"
        cell = Cell(cell.x + 1, cell.y - 1)

print(len(insiders))


def print_board():
    for y in range(min_y, max_y + 1):
        row = ""
        for x in range(min_x, max_x + 1):
            cell = Cell(x, y)
            if cell in path_as_set:
                row += "#"
            else:
                row += "."
        print(row)


def print_insiders():
    for y in range(min_y, max_y + 1):
        row = ""
        for x in range(min_x, max_x + 1):
            cell = Cell(x, y)
            if cell in insiders:
                row += "I"
            else:
                row += "."
        print(row)


# print_board()
# print('----')
# print_insiders()

# print(max(area_clockwise, area_counterclockwise))
# Find the inside of the path using Green's theorem
