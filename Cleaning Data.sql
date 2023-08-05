--Cleaning Data in SQL Queries

Select *
FROM "nashvillehousing"

-- Populate Property Address data

SELECT *
FROM "nashvillehousing"
--Where PropertyAddress is null
ORDER BY ParcelID


SELECT a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, COALESCE(a.PropertyAddress, b.PropertyAddress) AS MergedPropertyAddress
FROM nashvillehousing a
JOIN nashvillehousing b
    ON a.ParcelID = b.ParcelID
    AND a.UniqueID <> b.UniqueID
WHERE a.PropertyAddress IS NULL


UPDATE nashvillehousing a
SET PropertyAddress = COALESCE(a.PropertyAddress, b.PropertyAddress)
FROM nashvillehousing b
WHERE a.ParcelID = b.ParcelID
    AND a.UniqueID <> b.UniqueID
    AND a.PropertyAddress IS NULL;
	
	
-- Breaking out Address into individual columns(Address, City, State)


SELECT PropertyAddress
FROM nashvillehousing
-- where PropertyAddress is NULL
-- Order BY ParcelID

UPDATE nashvillehousing
SET PropertyAddress = SUBSTRING(PropertyAddress, 1, POSITION(',' IN PropertyAddress) - 1)
WHERE PropertyAddress LIKE '%,%';


ALTER TABlE nashvillehousing
Add PropertySplittAddress varchar(255)

UPDATE nashvillehousing
SET PropertySplittAddress = SPLIT_PART(PropertyAddress, ',', 1)
WHERE PropertyAddress LIKE '%,%';

ALTER TABlE nashvillehousing
Add PropertySplitCity varchar(255)

UPDATE nashvillehousing
SET PropertySplitCity = SUBSTRING(PropertyAddress, 1, strpos(PropertyAddress, ',') - 1)
WHERE PropertyAddress LIKE '%,%';




SELECT *
FROM nashvillehousing




SELECT OwnerAddress
FROM nashvillehousing


SELECT
    split_part(OwnerAddress, ',', 3) AS Country,
    split_part(OwnerAddress, ',', 2) AS State,
    split_part(OwnerAddress, ',', 1) AS City
FROM nashvillehousing;



ALTER TABLE NashvilleHousing
ADD OwnerSplitAddress varchar(255)

UPDATE NashvilleHousing
SET OwnerSplitAddress = split_part(OwnerAddress, ',', 3)

ALTER TABLE NashvilleHousing
ADD OwnerSplitCity varchar(255)

UPDATE NashvilleHousing
SET OwnerSplitAddress = split_part(OwnerAddress, ',', 2)


ALTER TABLE NashvilleHousing
ADD OwnerSplitState varchar(255)

UPDATE NashvilleHousing
SET OwnerSplitState = split_part(OwnerAddress, ',', 1)


SELECT *
FROM NashvilleHousing









-- Change Y and N to Yes and NO in "Sold as Vacant" field


SELECT Distinct(SoldAsVacant), COUNT(SoldAsVacant)
FROM NashvilleHousing
GROUP BY SoldAsVacant
Order By 2




SELECT SoldAsVacant
, CASE When SoldAsVacant = 'Y' THEN 'Yes'
       When SoldAsVacant = 'N' THEN 'No'
	   Else SoldAsVacant
	   END SoldAsVacant
FROM NashvilleHousing


UPDATE NashvilleHousing
SET SoldAsVacant = CASE When SoldAsVacant = 'Y' THEN 'Yes'
         When SoldAsVacant = 'N' THEN 'No'
		 ELSE SoldAsVacant
		 END
		 






-- Remove Duplicates

WITH RowNumCTE AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY ParcelID,
                            PropertyAddress,
                            SalePrice,
                            SaleDate,
                            LegalReference
               ORDER BY UniqueID
           ) AS row_num
    FROM nashvillehousing
)
SELECT *
FROM RowNumCTE
WHERE row_num > 1
ORDER BY PropertyAddress;







-- Delete Unused Columns


SELECT *
FROM nashvillehousing




ALTER TABLE nashvillehousing
DROP COLUMN OwnerAddress


ALTER TABLE nashvillehousing
DROP COLUMN TaxDistrict


ALTER TABLE nashvillehousing
DROP COLUMN PropertyAddress

ALTER TABLE nashvillehousing
DROP COLUMN SaleDate











		         
		




